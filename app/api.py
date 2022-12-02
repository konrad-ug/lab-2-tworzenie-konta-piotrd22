from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.KontoOsobiste import KontoOsobiste


app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    if RejestrKont.searchUserbyPesel(dane["pesel"]) != None:
        return jsonify("This PESEL is already in our DB"), 400

    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = KontoOsobiste(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.addUser(konto)
    return jsonify("Konto stworzone"), 201


@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    print("Request o ilosc kont")
    return jsonify(RejestrKont.usersCount()), 201


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    konto = RejestrKont.searchUserbyPesel(pesel)
    return jsonify(imie=konto.imie,  nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200


@app.route("/konta/konto/<pesel>", methods=["PUT"])
def updateAccount(pesel):
    updateData = request.get_json()
    konto = RejestrKont.updateUser(pesel, updateData)
    if konto == "You cannot change pesel!":
        return jsonify(konto), 200
    return jsonify(imie=konto.imie,  nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200


@app.route("/konta/konto/<pesel>", methods=["DELETE"])
def deleteAccount(pesel):
    res = RejestrKont.deleteUser(pesel)
    return jsonify(res), 200
