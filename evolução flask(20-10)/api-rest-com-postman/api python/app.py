
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 2, "titulo": "Harry Potter", "autor": "J.K. Rowling"},
    {"id": 3, "titulo": "O Alquimista", "autor": "Paulo Coelho"},
    {"id": 4, "titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"id": 5, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry"},
    {"id": 6, "titulo": "Percy Jackson e o Ladrão de Raios", "autor": "Rick Riordan"},
    {"id": 7, "titulo": "A Culpa é das Estrelas", "autor": "John Green"},
    {"id": 8, "titulo": "1984", "autor": "George Orwell"},
    {"id": 9, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien"},
    {"id": 10, "titulo": "Jogos Vorazes", "autor": "Suzanne Collins"}
]

# CONSULTAR TODOS OS LIVROS
@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros), 200

# CONSULTAR UM LIVRO PELO ID
@app.route("/livros/<int:id>", methods=["GET"])
def obter_livro_por_id(id):
    for livro in livros:
        if livro["id"] == id:
            return jsonify(livro), 200

    return jsonify({"erro": "Livro não encontrado"}), 404

# EDITAR LIVRO PELO ID
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livro_por_id(id):
    for livro in livros:
        if livro["id"] == id:
            dados = request.get_json()

            livro["titulo"] = dados["titulo"]
            livro["autor"] = dados["autor"]

            return jsonify(livro), 200

    return jsonify({"erro": "Livro não encontrado"}), 404


# INCLUIR NOVO LIVRO
@app.route("/livros", methods=["POST"])
def incluir_novo_livro():
    dados = request.get_json()

    novo_livro = {
        "id": max([livro["id"] for livro in livros], default=0) + 1,
        "titulo": dados["titulo"],
        "autor": dados["autor"]
    }

    livros.append(novo_livro)

    return jsonify(novo_livro), 201


# EXCLUIR LIVRO PELO ID
@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)
            return jsonify({"mensagem": "Livro excluído com sucesso"}), 200

    return jsonify({"erro": "Livro não encontrado"}), 404


# INICIALIZAÇÃO DO SERVIDOR
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)