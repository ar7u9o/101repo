mkT = (f) ->
    (val) ->
        try
            f(val)
        catch error
            val

gmapT = (f, val) ->
    if typeof val == 'number' or typeof val == 'string'
        val
    else
        for key, value of val
            val[key] = f(value)
        val

mkT = (f) ->
    (x) ->
        try
            f(x)
        catch error
            x
        
everywhere = (f) ->
    (x) ->
        f(gmapT(everywhere(f),x))

cut = ({ name, salary }) ->
    if salary? and name?
        name: name
        salary: salary / 2
        
    else
        throw "error"

research = 
    name: "Research"
    depts: [
        name: "Ralf"
        salary: 123456.0
    ]

company =
    name: "Meganalysis"
    depts: [research]


c = (everywhere mkT cut) company
console.log c.depts[0].depts

