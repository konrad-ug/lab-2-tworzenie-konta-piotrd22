import unittest
import requests


class TestOblusgaKont(unittest.TestCase):
    body = {
        "imie": "john",
        "nazwisko": "doe",
        "pesel": "02225432100"
    }

    url = "http://127.0.0.1:5000"

    def test_create_valid_account(self):
        create_resp = requests.post(
            self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(create_resp.status_code, 201)

    def test_get_account_fromPesel(self):
        get_resp = requests.get(
            self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)

        resp_body = get_resp.json()
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["imie"], self.body["imie"])
        self.assertEqual(resp_body["saldo"], 0)

    body_to_update = {
        "pesel": "0212345678",
        "imie": "joh",
        "nazwisko": "do",
    }

    def test_updateAccount(self):
        create_resp = requests.put(
            self.url + f"/konta/konto/{self.body['pesel']}", json=self.body_to_update
        )
        self.assertEqual(create_resp.status_code, 200)

        resp_body = create_resp.json()
        self.assertEqual(resp_body["imie"], "joh")
        self.assertEqual(resp_body["nazwisko"], "do")
        self.assertEqual(resp_body["saldo"], 0)
