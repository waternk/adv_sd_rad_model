import parsimonious

class FileParser(parsimonious.NodeVisitor):
        def __init__(self, ast):
            self.entries = []
            self.visit(ast)

        def visit_main(self, n, vc):
            self.entries.append({'name': '_main_',
                                 'params': [],
                                 'returns': [],
                                 'string': n.text.strip()})

        def visit_macro(self, n, vc):
            name = vc[2]
            params = vc[6]
            returns = vc[10]
            text = vc[13]
            self.entries.append({'name': name,
                                 'params': [x.strip() for x in params.split(',')] if params else [],
                                 'returns': [x.strip() for x in
                                             returns.split(',')] if returns else [],
                                 'string': text.strip()})

        def generic_visit(self, n, vc):
            return ''.join(filter(None, vc)) or n.text or ''