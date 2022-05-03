var name = 'father';
//var letter = 'Dear '+name+'\n\nLorem ipsum dolor sit amet, consectetur adipisicing '+name+' elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit '+name+' in voluptate father velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit '+name+' anim id est laborum. '+name+'';
//console.log(letter); → (before)
var letter = `Dear ${name}

Lorem ipsum dolor sit amet,
consectetur adipisicing ${name} elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit ${150+80} in voluptate father
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt mollit ${name} anim id est
laborum. ${name}`;

console.log(letter);
