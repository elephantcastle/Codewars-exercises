replaceAll = (input, find, replace) => input.replace(new RegExp(find.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, '\\$&'),"g"), replace);