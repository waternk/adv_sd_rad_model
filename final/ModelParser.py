import parsimonious

class ModelParser(parsimonious.NodeVisitor):
        def __init__(self, ast):
            self.entries = []
            self.visit(ast)

        def visit_entry(self, n, vc):
            self.entries.append({'eqn': vc[0].strip(),
                                 'unit': vc[2].strip(),
                                 'doc': vc[4].strip(),
                                 'kind': 'entry'})

        def visit_section(self, n, vc):
            if vc[2].strip() != "Simulation Control Parameters":
                self.entries.append({'eqn': '',
                                     'unit': '',
                                     'doc': vc[2].strip(),
                                     'kind': 'section'})

        def generic_visit(self, n, vc):
            return ''.join(filter(None, vc)) or n.text or ''