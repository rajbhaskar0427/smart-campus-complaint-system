import unittest
import json
from app import app
from database import get_db

class SmartCampusTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Smart Campus Complaint System', response.data)
        self.assertIn(b'Lloyd Institute', response.data)

    def test_demo_login_switch(self):
        # Test 1-click switch to student Bhaskar Raj
        res = self.client.get('/login?demo=student', follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Bhaskar Raj', res.data)

        # Test 1-click switch to admin Prof. Vishal Gupta
        res = self.client.get('/login?demo=admin', follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Administrator Console', res.data)

    def test_submit_new_complaint(self):
        with self.client.session_transaction() as sess:
            sess['user_id'] = 2
            sess['user_name'] = 'Bhaskar Raj'
            sess['user_role'] = 'student'

        post_data = {
            'user_name': 'Bhaskar Raj',
            'user_email': 'bhaskar@lloyd.ac.in',
            'user_roll': '2501530100041',
            'category': 'Internet & WiFi',
            'subcategory': 'Network Dropping',
            'building_block': 'Block B - CS Labs',
            'room_location': 'CS Lab 4',
            'title': 'High latency and packet drop on Switch 4',
            'description': 'Students cannot clone github repositories due to SSL timeout error.',
            'priority': 'High'
        }
        res = self.client.post('/submit', data=post_data, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Complaint registered successfully', res.data)
        self.assertIn(b'High latency and packet drop on Switch 4', res.data)

    def test_duplicate_check_api(self):
        req_body = {
            'building_block': 'Block B - CS Labs',
            'category': 'Internet & WiFi',
            'title': 'Wi-Fi disconnects in lab'
        }
        res = self.client.post('/api/check-duplicates', 
                                data=json.dumps(req_body), 
                                content_type='application/json')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn('duplicates', data)
        self.assertTrue(len(data['duplicates']) > 0)

    def test_simulation_endpoints(self):
        # 1. IoT Trigger
        res = self.client.post('/api/simulation/trigger-iot', 
                               data=json.dumps({}), 
                               content_type='application/json')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertIn('ticket_id', data)

        # 2. SLA Auto-Escalation
        res = self.client.post('/api/simulation/auto-escalate', 
                               data=json.dumps({}), 
                               content_type='application/json')
        self.assertEqual(res.status_code, 200)

        # 3. Resolve Demo
        res = self.client.post('/api/simulation/resolve-demo', 
                               data=json.dumps({}), 
                               content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_pages_render(self):
        endpoints = ['/track', '/analytics', '/simulation', '/qr-scanner', '/export/csv']
        for ep in endpoints:
            res = self.client.get(ep)
            self.assertEqual(res.status_code, 200, f"Endpoint {ep} failed with {res.status_code}")

if __name__ == '__main__':
    unittest.main()
