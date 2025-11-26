class KnowledgeGraph:
    def __init__(self):
        
        self.graph = {}

    
    def add_entity(self, entity_id, entity_type, properties=None):
        if entity_id in self.graph:
            print(f"Entidade '{entity_id}' já existe.")
            return
        
        self.graph[entity_id] = {
            "type": entity_type,
            "properties": properties if properties else {},
            "relations": {}
        }

    
    def add_relation(self, source, relation, target):
        if source not in self.graph:
            print(f"Entidade '{source}' não existe.")
            return
        if target not in self.graph:
            print(f"Entidade '{target}' não existe.")
            return
        
        if relation not in self.graph[source]["relations"]:
            self.graph[source]["relations"][relation] = []

        self.graph[source]["relations"][relation].append(target)

    
    def get_entity(self, entity_id):
        return self.graph.get(entity_id, None)

    
    def get_relations(self, entity_id):
        if entity_id not in self.graph:
            return None
        return self.graph[entity_id]["relations"]

    
    def remove_entity(self, entity_id):
        if entity_id not in self.graph:
            print("Entidade não encontrada.")
            return

        del self.graph[entity_id]

        
        for entity in self.graph.values():
            for rel_list in entity["relations"].values():
                if entity_id in rel_list:
                    rel_list.remove(entity_id)

    

    def remove_relation(self, source, relation, target):
        if source in self.graph and relation in self.graph[source]["relations"]:
            if target in self.graph[source]["relations"][relation]:
                self.graph[source]["relations"][relation].remove(target)

    

    def show_graph(self):
        for entity, data in self.graph.items():
            print(f"\n[{entity}] ({data['type']})")
            print(f"  Properties: {data['properties']}")
            print("  Relations:")
            for rel, targets in data["relations"].items():
                for t in targets:
                    print(f"    - {rel} -> {t}")





kg = KnowledgeGraph()

# Criando os times
kg.add_entity("Cruzeiro", "Time", {"cidade": "Minas Gerais"})
kg.add_entity("Atlético Mineiro", "Time", {"cidade": "Minas Gerais"})

# Criando os jogadores
kg.add_entity("Gabriel Barbosa", "Jogador", {"idade": 29, "posição": "Atacante"})
kg.add_entity("Dudu", "Jogador", {"idade": 33, "posição": "Ponta"})

# Criando os relacionamentos
kg.add_relation("Gabriel Barbosa", "joga_no", "Cruzeiro")
kg.add_relation("Dudu", "joga_no", "Atlético Mineiro")


kg.show_graph()
