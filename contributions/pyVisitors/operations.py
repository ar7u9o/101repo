import company


class Visitor(object):

    def visit(self, o):
        methname = "visit_%s" % o.__class__.__name__
        method = getattr(self, methname, self.default)
        method(o)

    def default(self, o):
        keys = filter(lambda i: not i.startswith('_'), i)
        for key in keys:
            self.visit(getattr(o, key))


class CutVisitor(Visitor):

    def visit_Company(self, c):
        for d in c.depts:
            self.visit(d)

    def visit_Department(self, d):
        self.visit(d.manager)
        for s in d.subunits:
            self.visit(s)

    def visit_Employee(self, e):
        e.salary /= 2.0

class TotalVisitor(Visitor):

    def __init__(self):
        Visitor.__init__(self)
        self.sum = 0

    def visit_Company(self, c):
        for d in c.depts:
            self.visit(d)

    def visit_Department(self, d):
        self.visit(d.manager)
        for s in d.subunits:
            self.visit(s)

    def visit_Employee(self, e):
        self.sum += e.salary

if __name__ == '__main__':
    t = TotalVisitor()
    t.visit(company.company)
    print t.sum

    CutVisitor().visit(company.company)

    t = TotalVisitor()
    t.visit(company.company)
    print t.sum

