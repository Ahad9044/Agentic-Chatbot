class GraphBuilder:
    def __init__(self, model):
        self.model = model

    def setup_graph(self, usecase: str):
        if not usecase:
            raise ValueError("Use case is required to set up the graph.")

        return {
            "model": self.model,
            "usecase": usecase,
        }
