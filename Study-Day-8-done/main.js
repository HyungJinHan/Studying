var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');
var template = require('./lib/Template.js');
var path = require('path');
var sanitizeHtml = require('sanitize-html');

/*var template = {
  html : function (title,list,body,control){
    return `
    <!doctype html>
    <html>
    <head>
      <title>WEB1 - ${title}</title>
      <meta charset="utf-8">
    </head>
    <body>
      <h1><a href="/">WEB</a></h1>
      ${list}
      ${control}
      ${body}
    </body>
    </html>
    `;
  },list:function (filelist){
    var list = '<ol>';
    var i = 0;
    while (i < filelist.length) {
      list = list + `<a href="/?id=${filelist[i]}"><li>${filelist[i]}</a></li>`;
      i = i + 1;
    }
    list = list+'</ol>';
    return list;
  }
}*/

var app = http.createServer(function(request,response){
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var pathname = url.parse(_url, true).pathname;

    /*
    function templatehtml(title,list,body,control){
      return `
      <!doctype html>
      <html>
      <head>
        <title>WEB1 - ${title}</title>
        <meta charset="utf-8">
      </head>
      <body>
        <h1><a href="/">WEB</a></h1>
        ${list}
        ${control}
        ${body}
      </body>
      </html>
      `;
    }

    function templatelist(filelist){
      var list = '<ol>';
      var i = 0;
      while (i < filelist.length) {
        list = list + `<a href="/?id=${filelist[i]}"><li>${filelist[i]}</a></li>`;
        i = i + 1;
      }
      list = list+'</ol>';
      return list;
    }
    */

    if(pathname === '/'){
      if(queryData.id === undefined){

        fs.readdir('./data', function(err, filelist){
          var title = 'Welcome';
          var description = 'Hello, HHJ';

          /*
          var list = templatelist(filelist);
          var template = templatehtml(title,list,
            `<h2>${title}</h2>${description}`,
            `<a href="/create">create</a>`
          );
          response.writeHead(200);
          response.end(template);
          */

          var list = template.list(filelist);
          var html = template.html(title,list,
            `<h2>${title}</h2>${description}`,
            `<a href="/create">create</a>`
          );
          response.writeHead(200);
          response.end(html);
        });
      } else {
        fs.readdir('./data', function(err, filelist){
          var filteredId = path.parse(queryData.id).base;
          fs.readFile(`data/${filteredId}`, 'utf8', function(err, description){
          var title = queryData.id;
          var sanitizedTitle = sanitizeHtml(title);
          var sanitizedDescription = sanitizeHtml(description);
          var list = template.list(filelist);
          var html = template.html(sanitizedTitle,list,
            `<h2>${sanitizedTitle}</h2>${sanitizedDescription}`,
            `<a href="/create">create</a>
             <a href="/update?id=${sanitizedTitle}">update</a>
             <form action="delete_process" method="post">
              <input type="hidden" name="id" value="${sanitizedTitle}">
              <input type="submit" value="delete">
             </form>`
          );
          response.writeHead(200);
          response.end(html);
        });
      });
    }
  } else if(pathname === '/create'){
    fs.readdir('./data', function(err, filelist){
      var title = 'WEB - Create';
      var list = template.list(filelist);
      var html = template.html(title,list,`
        <form action="/create_process" method="post">
          <p><input tupe="text" name="title" placeholder="제목"></p>
          <p>
            <textarea name="description" placeholder="내용"></textarea>
          </p>
          <p>
            <input type="submit">
          </p>
        </form>
        `,'');
      response.writeHead(200);
      response.end(html);
    });
  } else if(pathname === '/create_process'){
    var body = '';
    request.on('data',function(data){
      body = body + data;
    });
    request.on('end',function(){
      var post = qs.parse(body);
      var title = post.title;
      var description = post.description;
      fs.writeFile(`data/${title}`, description, 'utf8', function(err){
        response.writeHead(302, {Location: `/?id=${title}`});
        response.end();
      })
    });
  }
  else if (pathname === '/update'){
      fs.readdir('./data', function(err, filelist){
        var filteredId = path.parse(queryData.id).base;
        fs.readFile(`data/${filteredId}`, 'utf8', function(err, description){
        var title = queryData.id;
        var list = template.list(filelist);
        var html = template.html(title,list,
          `
          <form action="/update_process" method="post">
              <input type="hidden" name="id" value="${title}">
              <p><input type="text" name="title" placeholder="제목" value='${title}'></p>
              <p>
                <textarea name="description" placeholder="내용">${description}</textarea>
              </p>
              <p>
                <input type="submit">
              </p>
            </form>
          `,
          `<a href="/create">create</a> <a href="/update?id=${title}">update</a>`
        );
        response.writeHead(200);
        response.end(html);
      });
    });
  }
  else if (pathname === '/update_process'){
    var body = '';
    request.on('data',function(data){
      body = body + data;
    });
    request.on('end',function(){
      var post = qs.parse(body);
      var id = post.id;
      var title = post.title;
      var description = post.description;
      fs.rename(`data/${id}`,`data/${title}`,function(error){
        fs.writeFile(`data/${title}`, description, 'utf8', function(err){
          response.writeHead(302, {Location: `/?id=${title}`});
          response.end();
        })
      })
      console.log(post);
    });
  }
  else if (pathname === '/delete_process'){
    var body = '';
    request.on('data',function(data){
      body = body + data;
    });
    request.on('end',function(){
      var post = qs.parse(body);
      var id = post.id;
      var filteredId = path.parse(id).base;
      fs.unlink(`data/${filteredId}`,function(error){
        response.writeHead(302, {Location: `/`});
        response.end();
      })
    });
  }
  else {
      response.writeHead(200);
      response.end('Not Found');
    }


});
app.listen(3000);