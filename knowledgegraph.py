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
kg.add_entity("Flamengo", "Time", {"estado": "RJ"})
kg.add_entity("Palmeiras", "Time", {"estado": "SP"})
kg.add_entity("São Paulo", "Time", {"estado": "SP"})
kg.add_entity("Corinthians", "Time", {"estado": "SP"})
kg.add_entity("Cruzeiro", "Time", {"estado": "MG"})
kg.add_entity("Atlético Mineiro", "Time", {"estado": "MG"})

# Criando os jogadores
kg.add_entity("Gabriel Barbosa", "Jogador", {"idade": 29, "posição": "Atacante"})
kg.add_entity("Dudu", "Jogador", {"idade": 33, "posição": "Ponta"})
kg.add_entity("Hulk", "Jogador", {"idade": 38, "posição": "Atacante"})
kg.add_entity("Arrascaeta", "Jogador", {"idade": 30, "posição": "Meia"})
kg.add_entity("Raphael Veiga", "Jogador", {"idade": 28, "posição": "Meia"})
kg.add_entity("Calleri", "Jogador", {"idade": 30, "posição": "Atacante"})
kg.add_entity("Yuri Alberto", "Jogador", {"idade": 23, "posição": "Atacante"})
kg.add_entity("Paulinho", "Jogador", {"idade": 24, "posição": "Atacante"})
kg.add_entity("Everton Ribeiro", "Jogador", {"idade": 35, "posição": "Meia"})
kg.add_entity("Endrick", "Jogador", {"idade": 18, "posição": "Atacante"})
kg.add_entity("Wesley", "Jogador", {"idade": 20, "posição": "Ponta"})
kg.add_entity("Pedro", "Jogador", {"idade": 27, "posição": "Atacante"})
kg.add_entity("Bruno Henrique", "Jogador", {"idade": 33, "posição": "Ponta"})
kg.add_entity("Fábio", "Jogador", {"idade": 43, "posição": "Goleiro"})


# Técnicos
kg.add_entity("Tite", "Técnico", {"nacionalidade": "Brasil"})
kg.add_entity("Abel Ferreira", "Técnico", {"nacionalidade": "Portugal"})
kg.add_entity("Felipão", "Técnico", {"nacionalidade": "Brasil"})

# Campeonato
kg.add_entity("Brasileirão Série A", "Campeonato", {"nível": "1"})

# Criando os relacionamentos
kg.add_relation("Gabriel Barbosa", "joga_no", "Flamengo")
kg.add_relation("Arrascaeta", "joga_no", "Flamengo")
kg.add_relation("Pedro", "joga_no", "Flamengo")
kg.add_relation("Bruno Henrique", "joga_no", "Flamengo")

kg.add_relation("Raphael Veiga", "joga_no", "Palmeiras")
kg.add_relation("Dudu", "joga_no", "Palmeiras")
kg.add_relation("Endrick", "joga_no", "Palmeiras")

kg.add_relation("Calleri", "joga_no", "São Paulo")
kg.add_relation("Wesley", "joga_no", "São Paulo")

kg.add_relation("Yuri Alberto", "joga_no", "Corinthians")

kg.add_relation("Hulk", "joga_no", "Atlético Mineiro")
kg.add_relation("Paulinho", "joga_no", "Atlético Mineiro")

kg.add_relation("Fábio", "joga_no", "Cruzeiro")


# Técnicos nos times
kg.add_relation("Tite", "treina", "Flamengo")
kg.add_relation("Abel Ferreira", "treina", "Palmeiras")
kg.add_relation("Felipão", "treina", "Atlético Mineiro")

# Times disputam campeonato
kg.add_relation("Flamengo", "disputa", "Brasileirão Série A")
kg.add_relation("Palmeiras", "disputa", "Brasileirão Série A")
kg.add_relation("Atlético Mineiro", "disputa", "Brasileirão Série A")
kg.add_relation("Cruzeiro", "disputa", "Brasileirão Série A")

kg.show_graph()



