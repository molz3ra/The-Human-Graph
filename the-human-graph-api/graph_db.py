from neo4j import GraphDatabase

# Credenciais do seu arquivo AuraDB
NEO4J_URI = "neo4j+s://4fa2400b.databases.neo4j.io"
NEO4J_USER = "4fa2400b" # <--- MUDE ISTO AQUI
NEO4J_PASSWORD = "s1tm47dRwfaIsbSAXgmbiz2geR8pbWsmIsADA9UCy1Q"

# ... (o resto do código fica igualzinho)

class Neo4jConnection:
    def __init__(self, uri, user, pwd):
        self.driver = GraphDatabase.driver(uri, auth=(user, pwd))

    def close(self):
        if self.driver is not None:
            self.driver.close()

    def criar_usuario_no_grafo(self, usuario_id: int, nome: str, departamento: str):
        query = """
        MERGE (u:Colaborador {id: $id})
        SET u.nome = $nome, u.departamento = $departamento
        RETURN u
        """
        with self.driver.session() as session:
            session.run(query, id=usuario_id, nome=nome, departamento=departamento)

    def criar_feedback_no_grafo(self, remetente_id: int, destinatario_id: int, competencia: str, score_risco: float):
        query = """
        MATCH (remetente:Colaborador {id: $remetente_id})
        MATCH (destinatario:Colaborador {id: $destinatario_id})
        MERGE (remetente)-[r:ENVIOU_FEEDBACK]->(destinatario)
        SET r.competencia = $competencia, r.risco = $score_risco
        RETURN r
        """
        with self.driver.session() as session:
            session.run(query, remetente_id=remetente_id, destinatario_id=destinatario_id, competencia=competencia, score_risco=score_risco)

graph_conn = Neo4jConnection(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)