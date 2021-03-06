gmapQ = (f, val) ->
    if typeof val == 'number' or typeof val == 'string'
        []
    else
        (f v) for k, v of val

everything = (r, f) ->
    (x) ->
        result = gmapQ everything(r, f), x
        result.push (f x)
        result.reduce r

mkQ = (base, specific) ->
    (x) ->
        try
            specific x
        catch error
            base

mkT = (f) ->
    (val) ->
        try
            f val
        catch error
            val

gmapT = (f, val) ->
    if typeof val == 'number' or typeof val == 'string'
        val
    else
        r = {}
        for key, value of val
            r[key] = f value
        r

mkT = (f) ->
    (x) ->
        try
            f x
        catch error
            x
        
everywhere = (f) ->
    (x) ->
        f gmapT(everywhere(f), x)

research = 
    name: "Research"
    depts: [
        name: "Ralf"
        salary: 123456.0
    ]

company =
    name: "Meganalysis"
    depts: [research]



cutE = ({ name, salary }) ->
    if salary? and name?
        name: name
        salary: salary / 2
        
    else
        throw "fail"
        
totalE = ({ name, salary }) ->
    if salary? and name?
        salary
    else
        throw "fail"

add = (a, b) -> a + b

total = everything add, (mkQ 0, totalE)
cut = everywhere mkT cutE

console.log total company

c = cut company
console.log total c

if (total c) != (total company) / 2.0
    console.log 'test failed'

