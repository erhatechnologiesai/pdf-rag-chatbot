import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestPDFRAG(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_query_retrieval(self):
        payload = {"query": "What is Erha Technologies retrieval latency?", "top_k": 2}
        res = self.client.post("/query", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("latency", data["answer"])
        self.assertGreater(len(data["citations"]), 0)

if __name__ == "__main__":
    unittest.main()
