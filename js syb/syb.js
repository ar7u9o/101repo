function id(x) {
    return x;
}

function everywhere(f) {

    return function(x) {
        return f(gmapT(everywhere(f), x))
    }

}

function gmapT(f, val) {

    if(typeof val == 'number' || typeof val == 'string') {
        return val;
    }
    
    else {

        for(key in val) {

            value = val[key];
            val[key] = f(value);
        }
        return val;

    }

}

function mkT(f) {

    return function(val) {
        try {
            return f(val);
        }
        catch(exc) {
            return val;
        }

    }

}

company = {

    name: 'Meganalysis',
    depts: [

        {
            salary: 12345,
            name : 'Ralf'
        }

    ]

}


function cutOne(e) {
    if(e.salary != null) {
        return {
            salary: e.salary/2,
            name: e.name
        };
    }
    else {
        throw new Error("wrong type");
    }
}
 
cut = everywhere(mkT(cutOne))
cut_company = cut(company);
console.log(cut_company)





