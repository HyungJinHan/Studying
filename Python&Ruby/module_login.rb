module Module_login
  module_function()
  def login(id)
    fam = ["hsh", "jhs", "hhj1", "hhj2"]
    for item in fam do
      if item == id
        return true
      end
    end
    return false
  end
end
