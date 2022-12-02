import unittest
import requests


class TestOblusgaKont(unittest.TestCase):
    body = {
        "imie": "john",
        "nazwisko": "doe",
        "pesel": "02225432100"
    }

    invalid_pesel = "1234567890"

    url = "http://127.0.0.1:5000"

    def test_create_valid_account(self):
        create_resp = requests.post(
            self.url + "/konta/stworz_konto", json=self.body
        )
        self.assertEqual(create_resp.status_code, 201)

    def test_get_account_fromPesel(self):
        get_resp = requests.get(
            self.url + f"/konta/konto/{self.body['pesel']}"
        )
        self.assertEqual(get_resp.status_code, 200)

        resp_body = get_resp.json()
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["imie"], self.body["imie"])
        self.assertEqual(resp_body["saldo"], 0)

    def test_get_account_fromInvalidPesel(self):
        get_resp = requests.get(
            self.url + f"/konta/konto/{self.invalid_pesel}"
        )
        self.assertEqual(get_resp.status_code, 400)

        resp_body = get_resp.json()
        self.assertEqual(resp_body, "There is no user with this PESEL")

    body_to_update = {
        "imie": "anakin",
        "nazwisko": "skylwalker",
        "saldo": 1
    }

    def test_updateAccount_valid(self):
        create_resp = requests.put(
            self.url + f"/konta/konto/{self.body['pesel']}", json=self.body_to_update
        )
        self.assertEqual(create_resp.status_code, 200)

        resp_body = create_resp.json()
        self.assertEqual(resp_body["imie"], self.body_to_update["imie"])
        self.assertEqual(resp_body["nazwisko"],
                         self.body_to_update["nazwisko"])
        self.assertEqual(resp_body["saldo"], 1)

    def test_update_fromInvalidPesel(self):
        get_resp = requests.put(
            self.url +
            f"/konta/konto/{self.invalid_pesel}", json=self.body_to_update
        )
        self.assertEqual(get_resp.status_code, 400)

        resp_body = get_resp.json()
        self.assertEqual(resp_body, "There is no user with this PESEL")

    body_to_update_2 = {
        "imie": "anakin",
        "nazwisko": "skylwalker",
        "pesel": "0212345678"
    }

    def test_updateAccount_unvalid(self):
        create_resp = requests.put(
            self.url + f"/konta/konto/{self.body['pesel']}", json=self.body_to_update_2
        )
        self.assertEqual(create_resp.status_code, 200)
        resp_body = create_resp.json()
        self.assertEqual(resp_body, "You cannot change pesel!")

    body_toDelete = {
        "imie": "john",
        "nazwisko": "doe",
        "pesel": "02225432101"
    }

    def test_deleteAccount(self):
        create_resp = requests.post(
            self.url + "/konta/stworz_konto", json=self.body_toDelete
        )
        self.assertEqual(create_resp.status_code, 201)

        create_resp = requests.delete(
            self.url + f"/konta/konto/{self.body_toDelete['pesel']}")
        self.assertEqual(create_resp.status_code, 200)

        resp_body = create_resp.json()
        self.assertEqual(resp_body, "User has been deleted")

    def test_delete_fromInvalidPesel(self):
        get_resp = requests.delete(
            self.url + f"/konta/konto/{self.invalid_pesel}"
        )
        self.assertEqual(get_resp.status_code, 400)

        resp_body = get_resp.json()
        self.assertEqual(resp_body, "There is no user with this PESEL")

    def test_notUniquePesel(self):
        create_resp = requests.post(
            self.url + "/konta/stworz_konto", json=self.body
        )
        self.assertEqual(create_resp.status_code, 400)

        resp_body = create_resp.json()
        self.assertEqual(resp_body, "This PESEL is already in our DB")
