function coordinates(p1,p2, p){
  var d = Math.sqrt(Math.pow(p1[1] - p2[1],2) + Math.pow(p1[0] - p2[0],2))

  return p ? Number(d.toFixed(p)) : Math.round(d)
}