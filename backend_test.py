#!/usr/bin/env python3
"""
Comprehensive Backend API Testing for WitchCraft: Sorcerers and Nahuals
Tests all backend APIs for functionality, data persistence, and error handling.
"""

import requests
import json
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Any
import uuid

# Backend URL from environment
BACKEND_URL = "https://f19fbab6-60c6-41d8-a5ff-60fbd1afa640.preview.emergentagent.com/api"

class WitchCraftAPITester:
    def __init__(self):
        self.base_url = BACKEND_URL
        self.session = requests.Session()
        self.test_results = []
        self.created_ids = {
            'technical_specs': [],
            'game_mechanics': [],
            'concept_art': [],
            'team_members': [],
            'roadmap': [],
            'publisher_data': [],
            'progress_metrics': []
        }
    
    def log_test(self, test_name: str, success: bool, details: str = ""):
        """Log test results"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if details:
            print(f"   Details: {details}")
        
        self.test_results.append({
            'test': test_name,
            'success': success,
            'details': details
        })
    
    def test_api_health(self):
        """Test basic API connectivity"""
        try:
            response = self.session.get(f"{self.base_url}/")
            if response.status_code == 200:
                data = response.json()
                self.log_test("API Health Check", True, f"API responding: {data.get('message', 'OK')}")
                return True
            else:
                self.log_test("API Health Check", False, f"Status: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("API Health Check", False, f"Connection error: {str(e)}")
            return False
    
    def test_technical_specs_api(self):
        """Test Technical Specifications API"""
        print("\n=== Testing Technical Specifications API ===")
        
        # Test CREATE
        test_spec = {
            "title": "WitchCraft UE5 Technical Specifications",
            "engine": "Unreal Engine 5",
            "version": "5.4",
            "platforms": ["PC", "PlayStation 5", "Xbox Series X/S"],
            "features": {
                "rendering": "Lumen Global Illumination",
                "physics": "Chaos Physics System",
                "audio": "MetaSounds",
                "networking": "Dedicated Servers"
            },
            "requirements": {
                "minimum_ram": "16GB",
                "recommended_gpu": "RTX 3070",
                "storage": "50GB SSD"
            }
        }
        
        try:
            response = self.session.post(f"{self.base_url}/technical-specs", json=test_spec)
            if response.status_code == 200:
                created_spec = response.json()
                spec_id = created_spec['id']
                self.created_ids['technical_specs'].append(spec_id)
                self.log_test("Technical Specs - CREATE", True, f"Created spec with ID: {spec_id}")
            else:
                self.log_test("Technical Specs - CREATE", False, f"Status: {response.status_code}, Response: {response.text}")
                return
        except Exception as e:
            self.log_test("Technical Specs - CREATE", False, f"Error: {str(e)}")
            return
        
        # Test GET ALL
        try:
            response = self.session.get(f"{self.base_url}/technical-specs")
            if response.status_code == 200:
                specs = response.json()
                self.log_test("Technical Specs - GET ALL", True, f"Retrieved {len(specs)} specifications")
            else:
                self.log_test("Technical Specs - GET ALL", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Technical Specs - GET ALL", False, f"Error: {str(e)}")
        
        # Test GET BY ID
        try:
            response = self.session.get(f"{self.base_url}/technical-specs/{spec_id}")
            if response.status_code == 200:
                spec = response.json()
                self.log_test("Technical Specs - GET BY ID", True, f"Retrieved spec: {spec['title']}")
            else:
                self.log_test("Technical Specs - GET BY ID", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Technical Specs - GET BY ID", False, f"Error: {str(e)}")
    
    def test_game_mechanics_api(self):
        """Test Game Mechanics API"""
        print("\n=== Testing Game Mechanics API ===")
        
        # Test CREATE
        test_mechanic = {
            "name": "Nahual Transformation",
            "description": "Players can transform into animal spirits with unique abilities",
            "category": "transformation",
            "implementation_details": "Blueprint-based transformation system with particle effects",
            "priority": "high",
            "status": "in_development"
        }
        
        try:
            response = self.session.post(f"{self.base_url}/game-mechanics", json=test_mechanic)
            if response.status_code == 200:
                created_mechanic = response.json()
                mechanic_id = created_mechanic['id']
                self.created_ids['game_mechanics'].append(mechanic_id)
                self.log_test("Game Mechanics - CREATE", True, f"Created mechanic: {created_mechanic['name']}")
            else:
                self.log_test("Game Mechanics - CREATE", False, f"Status: {response.status_code}, Response: {response.text}")
                return
        except Exception as e:
            self.log_test("Game Mechanics - CREATE", False, f"Error: {str(e)}")
            return
        
        # Test GET ALL
        try:
            response = self.session.get(f"{self.base_url}/game-mechanics")
            if response.status_code == 200:
                mechanics = response.json()
                self.log_test("Game Mechanics - GET ALL", True, f"Retrieved {len(mechanics)} mechanics")
            else:
                self.log_test("Game Mechanics - GET ALL", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Game Mechanics - GET ALL", False, f"Error: {str(e)}")
        
        # Test UPDATE
        try:
            update_data = {
                "name": "Enhanced Nahual Transformation",
                "description": "Updated transformation system with improved visual effects",
                "category": "transformation",
                "implementation_details": "Enhanced Blueprint system with advanced particle effects",
                "priority": "critical",
                "status": "testing"
            }
            response = self.session.put(f"{self.base_url}/game-mechanics/{mechanic_id}", json=update_data)
            if response.status_code == 200:
                updated_mechanic = response.json()
                self.log_test("Game Mechanics - UPDATE", True, f"Updated mechanic: {updated_mechanic['name']}")
            else:
                self.log_test("Game Mechanics - UPDATE", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Game Mechanics - UPDATE", False, f"Error: {str(e)}")
    
    def test_concept_art_api(self):
        """Test Concept Art API"""
        print("\n=== Testing Concept Art API ===")
        
        # Test CREATE
        test_art = {
            "title": "Witch Character Design",
            "description": "Main protagonist witch character with mystical robes",
            "category": "character",
            "image_url": "https://example.com/witch-concept.jpg",
            "artist": "Elena Mystique",
            "tags": ["character", "protagonist", "witch", "mystical"]
        }
        
        try:
            response = self.session.post(f"{self.base_url}/concept-art", json=test_art)
            if response.status_code == 200:
                created_art = response.json()
                art_id = created_art['id']
                self.created_ids['concept_art'].append(art_id)
                self.log_test("Concept Art - CREATE", True, f"Created art: {created_art['title']}")
            else:
                self.log_test("Concept Art - CREATE", False, f"Status: {response.status_code}, Response: {response.text}")
                return
        except Exception as e:
            self.log_test("Concept Art - CREATE", False, f"Error: {str(e)}")
            return
        
        # Test GET ALL
        try:
            response = self.session.get(f"{self.base_url}/concept-art")
            if response.status_code == 200:
                art_list = response.json()
                self.log_test("Concept Art - GET ALL", True, f"Retrieved {len(art_list)} artworks")
            else:
                self.log_test("Concept Art - GET ALL", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Concept Art - GET ALL", False, f"Error: {str(e)}")
        
        # Test GET BY CATEGORY
        try:
            response = self.session.get(f"{self.base_url}/concept-art/category/character")
            if response.status_code == 200:
                character_art = response.json()
                self.log_test("Concept Art - GET BY CATEGORY", True, f"Retrieved {len(character_art)} character artworks")
            else:
                self.log_test("Concept Art - GET BY CATEGORY", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Concept Art - GET BY CATEGORY", False, f"Error: {str(e)}")
    
    def test_team_members_api(self):
        """Test Team Members API"""
        print("\n=== Testing Team Members API ===")
        
        # Test CREATE
        test_member = {
            "name": "Carlos Shadowweaver",
            "role": "lead_programmer",
            "bio": "Senior developer with 10+ years in game development",
            "skills": ["C++", "Unreal Engine", "Blueprint", "Networking"],
            "contact": "carlos@witchcraft-game.com",
            "avatar_url": "https://example.com/carlos-avatar.jpg"
        }
        
        try:
            response = self.session.post(f"{self.base_url}/team-members", json=test_member)
            if response.status_code == 200:
                created_member = response.json()
                member_id = created_member['id']
                self.created_ids['team_members'].append(member_id)
                self.log_test("Team Members - CREATE", True, f"Created member: {created_member['name']}")
            else:
                self.log_test("Team Members - CREATE", False, f"Status: {response.status_code}, Response: {response.text}")
                return
        except Exception as e:
            self.log_test("Team Members - CREATE", False, f"Error: {str(e)}")
            return
        
        # Test GET ALL
        try:
            response = self.session.get(f"{self.base_url}/team-members")
            if response.status_code == 200:
                members = response.json()
                self.log_test("Team Members - GET ALL", True, f"Retrieved {len(members)} team members")
            else:
                self.log_test("Team Members - GET ALL", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Team Members - GET ALL", False, f"Error: {str(e)}")
        
        # Test GET BY ID
        try:
            response = self.session.get(f"{self.base_url}/team-members/{member_id}")
            if response.status_code == 200:
                member = response.json()
                self.log_test("Team Members - GET BY ID", True, f"Retrieved member: {member['name']}")
            else:
                self.log_test("Team Members - GET BY ID", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Team Members - GET BY ID", False, f"Error: {str(e)}")
    
    def test_roadmap_api(self):
        """Test Roadmap API"""
        print("\n=== Testing Roadmap API ===")
        
        # Test CREATE
        start_date = datetime.utcnow()
        end_date = start_date + timedelta(days=30)
        
        test_roadmap = {
            "title": "Combat System Implementation",
            "description": "Implement core combat mechanics and spell casting",
            "milestone": "Alpha Release",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "status": "in_development",
            "priority": "high",
            "assigned_to": [],
            "dependencies": [],
            "progress": 25
        }
        
        try:
            response = self.session.post(f"{self.base_url}/roadmap", json=test_roadmap)
            if response.status_code == 200:
                created_item = response.json()
                roadmap_id = created_item['id']
                self.created_ids['roadmap'].append(roadmap_id)
                self.log_test("Roadmap - CREATE", True, f"Created roadmap item: {created_item['title']}")
            else:
                self.log_test("Roadmap - CREATE", False, f"Status: {response.status_code}, Response: {response.text}")
                return
        except Exception as e:
            self.log_test("Roadmap - CREATE", False, f"Error: {str(e)}")
            return
        
        # Test GET ALL
        try:
            response = self.session.get(f"{self.base_url}/roadmap")
            if response.status_code == 200:
                roadmap_items = response.json()
                self.log_test("Roadmap - GET ALL", True, f"Retrieved {len(roadmap_items)} roadmap items")
            else:
                self.log_test("Roadmap - GET ALL", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Roadmap - GET ALL", False, f"Error: {str(e)}")
        
        # Test UPDATE PROGRESS
        try:
            response = self.session.put(f"{self.base_url}/roadmap/{roadmap_id}/progress?progress=75")
            if response.status_code == 200:
                updated_item = response.json()
                self.log_test("Roadmap - UPDATE PROGRESS", True, f"Updated progress to {updated_item['progress']}%")
            else:
                self.log_test("Roadmap - UPDATE PROGRESS", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Roadmap - UPDATE PROGRESS", False, f"Error: {str(e)}")
    
    def test_publisher_data_api(self):
        """Test Publisher Data API"""
        print("\n=== Testing Publisher Data API ===")
        
        # Test CREATE
        test_publisher_data = {
            "section": "market_analysis",
            "title": "Target Market Analysis",
            "content": "WitchCraft targets the growing SRPG market with unique Mexican folklore elements",
            "data": {
                "market_size": "$2.1B",
                "target_demographics": ["18-35", "RPG enthusiasts", "Indie game fans"],
                "competitive_advantage": "Unique cultural setting and transformation mechanics"
            },
            "order": 1
        }
        
        try:
            response = self.session.post(f"{self.base_url}/publisher-data", json=test_publisher_data)
            if response.status_code == 200:
                created_data = response.json()
                publisher_id = created_data['id']
                self.created_ids['publisher_data'].append(publisher_id)
                self.log_test("Publisher Data - CREATE", True, f"Created publisher data: {created_data['title']}")
            else:
                self.log_test("Publisher Data - CREATE", False, f"Status: {response.status_code}, Response: {response.text}")
                return
        except Exception as e:
            self.log_test("Publisher Data - CREATE", False, f"Error: {str(e)}")
            return
        
        # Test GET ALL
        try:
            response = self.session.get(f"{self.base_url}/publisher-data")
            if response.status_code == 200:
                publisher_data = response.json()
                self.log_test("Publisher Data - GET ALL", True, f"Retrieved {len(publisher_data)} publisher data items")
            else:
                self.log_test("Publisher Data - GET ALL", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Publisher Data - GET ALL", False, f"Error: {str(e)}")
        
        # Test GET BY SECTION
        try:
            response = self.session.get(f"{self.base_url}/publisher-data/section/market_analysis")
            if response.status_code == 200:
                section_data = response.json()
                self.log_test("Publisher Data - GET BY SECTION", True, f"Retrieved {len(section_data)} market analysis items")
            else:
                self.log_test("Publisher Data - GET BY SECTION", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Publisher Data - GET BY SECTION", False, f"Error: {str(e)}")
    
    def test_progress_metrics_api(self):
        """Test Progress Metrics API"""
        print("\n=== Testing Progress Metrics API ===")
        
        # Test CREATE
        test_metric = {
            "metric_name": "Combat System Completion",
            "current_value": 65.0,
            "target_value": 100.0,
            "unit": "percentage",
            "category": "development"
        }
        
        try:
            response = self.session.post(f"{self.base_url}/progress-metrics", json=test_metric)
            if response.status_code == 200:
                created_metric = response.json()
                metric_id = created_metric['id']
                self.created_ids['progress_metrics'].append(metric_id)
                self.log_test("Progress Metrics - CREATE", True, f"Created metric: {created_metric['metric_name']}")
            else:
                self.log_test("Progress Metrics - CREATE", False, f"Status: {response.status_code}, Response: {response.text}")
                return
        except Exception as e:
            self.log_test("Progress Metrics - CREATE", False, f"Error: {str(e)}")
            return
        
        # Test GET ALL
        try:
            response = self.session.get(f"{self.base_url}/progress-metrics")
            if response.status_code == 200:
                metrics = response.json()
                self.log_test("Progress Metrics - GET ALL", True, f"Retrieved {len(metrics)} progress metrics")
            else:
                self.log_test("Progress Metrics - GET ALL", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Progress Metrics - GET ALL", False, f"Error: {str(e)}")
        
        # Test GET BY CATEGORY
        try:
            response = self.session.get(f"{self.base_url}/progress-metrics/category/development")
            if response.status_code == 200:
                dev_metrics = response.json()
                self.log_test("Progress Metrics - GET BY CATEGORY", True, f"Retrieved {len(dev_metrics)} development metrics")
            else:
                self.log_test("Progress Metrics - GET BY CATEGORY", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Progress Metrics - GET BY CATEGORY", False, f"Error: {str(e)}")
        
        # Test UPDATE
        try:
            response = self.session.put(f"{self.base_url}/progress-metrics/{metric_id}?current_value=85.0")
            if response.status_code == 200:
                updated_metric = response.json()
                self.log_test("Progress Metrics - UPDATE", True, f"Updated metric value to {updated_metric['current_value']}")
            else:
                self.log_test("Progress Metrics - UPDATE", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_test("Progress Metrics - UPDATE", False, f"Error: {str(e)}")
    
    def test_dashboard_summary_api(self):
        """Test Dashboard Summary API - Critical for frontend dashboard"""
        print("\n=== Testing Dashboard Summary API ===")
        
        try:
            response = self.session.get(f"{self.base_url}/dashboard-summary")
            if response.status_code == 200:
                summary = response.json()
                
                # Validate response structure
                required_fields = ['project_name', 'overview', 'last_updated']
                overview_fields = ['total_mechanics', 'completed_mechanics', 'mechanics_progress', 
                                 'total_roadmap_items', 'completed_roadmap_items', 'roadmap_progress',
                                 'overall_progress', 'total_concept_art', 'team_size']
                
                missing_fields = []
                for field in required_fields:
                    if field not in summary:
                        missing_fields.append(field)
                
                for field in overview_fields:
                    if field not in summary.get('overview', {}):
                        missing_fields.append(f"overview.{field}")
                
                if missing_fields:
                    self.log_test("Dashboard Summary - STRUCTURE", False, f"Missing fields: {missing_fields}")
                else:
                    self.log_test("Dashboard Summary - STRUCTURE", True, "All required fields present")
                
                # Validate data types and values
                overview = summary.get('overview', {})
                data_valid = True
                validation_errors = []
                
                # Check numeric fields
                numeric_fields = ['total_mechanics', 'completed_mechanics', 'total_roadmap_items', 
                                'completed_roadmap_items', 'total_concept_art', 'team_size']
                for field in numeric_fields:
                    if field in overview and not isinstance(overview[field], (int, float)):
                        validation_errors.append(f"{field} should be numeric")
                        data_valid = False
                
                # Check percentage fields
                percentage_fields = ['mechanics_progress', 'roadmap_progress', 'overall_progress']
                for field in percentage_fields:
                    if field in overview:
                        value = overview[field]
                        if not isinstance(value, (int, float)) or value < 0 or value > 100:
                            validation_errors.append(f"{field} should be 0-100")
                            data_valid = False
                
                if data_valid:
                    self.log_test("Dashboard Summary - DATA VALIDATION", True, "All data types and ranges valid")
                else:
                    self.log_test("Dashboard Summary - DATA VALIDATION", False, f"Validation errors: {validation_errors}")
                
                self.log_test("Dashboard Summary - GET", True, f"Project: {summary.get('project_name', 'Unknown')}")
                
            else:
                self.log_test("Dashboard Summary - GET", False, f"Status: {response.status_code}, Response: {response.text}")
        except Exception as e:
            self.log_test("Dashboard Summary - GET", False, f"Error: {str(e)}")
    
    def test_error_handling(self):
        """Test error handling for invalid requests"""
        print("\n=== Testing Error Handling ===")
        
        # Test 404 for non-existent resources
        fake_id = str(uuid.uuid4())
        
        endpoints_to_test = [
            f"/technical-specs/{fake_id}",
            f"/game-mechanics/{fake_id}",
            f"/team-members/{fake_id}",
            f"/roadmap/{fake_id}/progress?progress=50"
        ]
        
        for endpoint in endpoints_to_test:
            try:
                response = self.session.get(f"{self.base_url}{endpoint}")
                if response.status_code == 404:
                    self.log_test(f"Error Handling - 404 {endpoint}", True, "Correctly returned 404")
                else:
                    self.log_test(f"Error Handling - 404 {endpoint}", False, f"Expected 404, got {response.status_code}")
            except Exception as e:
                self.log_test(f"Error Handling - 404 {endpoint}", False, f"Error: {str(e)}")
        
        # Test invalid progress update
        if self.created_ids['roadmap']:
            roadmap_id = self.created_ids['roadmap'][0]
            try:
                response = self.session.put(f"{self.base_url}/roadmap/{roadmap_id}/progress?progress=150")
                if response.status_code == 400:
                    self.log_test("Error Handling - Invalid Progress", True, "Correctly rejected invalid progress value")
                else:
                    self.log_test("Error Handling - Invalid Progress", False, f"Expected 400, got {response.status_code}")
            except Exception as e:
                self.log_test("Error Handling - Invalid Progress", False, f"Error: {str(e)}")
    
    def run_all_tests(self):
        """Run all API tests"""
        print("🧙‍♀️ Starting WitchCraft Backend API Tests 🧙‍♀️")
        print("=" * 60)
        
        # Test API health first
        if not self.test_api_health():
            print("❌ API is not responding. Aborting tests.")
            return False
        
        # Run all API tests
        self.test_technical_specs_api()
        self.test_game_mechanics_api()
        self.test_concept_art_api()
        self.test_team_members_api()
        self.test_roadmap_api()
        self.test_publisher_data_api()
        self.test_progress_metrics_api()
        self.test_dashboard_summary_api()
        self.test_error_handling()
        
        # Print summary
        print("\n" + "=" * 60)
        print("🧙‍♀️ TEST SUMMARY 🧙‍♀️")
        print("=" * 60)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['success'])
        failed_tests = total_tests - passed_tests
        
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        if failed_tests > 0:
            print("\n❌ FAILED TESTS:")
            for result in self.test_results:
                if not result['success']:
                    print(f"  - {result['test']}: {result['details']}")
        
        return failed_tests == 0

if __name__ == "__main__":
    tester = WitchCraftAPITester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)