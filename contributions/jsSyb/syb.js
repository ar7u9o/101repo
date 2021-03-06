function id(x) {
    return x;
}

function everywhere(f) {

    return function(x) {
        return f(gmapT(everywhere(f), x));
    }

}

function foldl(f, data) {
    var acc = data[0];
    for(var i=1; i<data.length; i++) {
        acc = f(acc, data[i]);
    }
    return acc;

}

function everything(r, f) {

    return function(x) {
        var result = gmapQ(everything(r, f), x);
        result.push(f(x));
        return foldl(r, result);
    };

}

function gmapQ(f, val) {

    if(typeof val == 'number' || typeof val == 'string') {
        return [];
    }
    else {
        var result = []
        for(key in val) {
            result.push(f(val[key]));
        }
        return result;
    }

}

function mkQ(base, specific) {

    return function(val) {
        try {
            return specific(val);
        }
        catch(exc) {
            if(exc != 'fail') {
                throw exc;
            }
            return base(val);
        }

    }

}

function const_(x) {

    return function() {
        return x;
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
            if(exc != 'fail') {
                throw exc;
            }
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
        throw 'fail';
    }
}

function getSalary(e) {

    if(e.salary != null) {
        return e.salary;
    }
    else {
        throw 'fail';
    }

}

total = everything(function (a, b) { return a+b; }, mkQ(const_(0), getSalary));
console.log(total(company));
 
cut = everywhere(mkT(cutOne));
cut_company = cut(company);
console.log(total(cut_company));





