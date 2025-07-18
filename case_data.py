import json
from typing import Dict, List, Optional

class CaseData:
    def __init__(self):
        self.cases = self._load_cases()
    
    def _load_cases(self) -> List[Dict]:
        """Load case data from file or create default cases"""
        # Default cases data
        cases = [
            {
                "id": 1,
                "title": "The Locked Room Mystery",
                "description": "A wealthy businessman found dead in his locked study",
                "difficulty": "Medium",
                "time_limit": 480,  # 8 minutes
                "location": "Mansion Study",
                "date": "October 15, 2023",
                "summary": "Victor Blackwood was found dead in his locked study with a gunshot wound. The door was locked from the inside, and the key was found in his pocket. Three people were in the house at the time of death.",
                "victim": {
                    "name": "Victor Blackwood",
                    "age": 58,
                    "occupation": "Business Owner",
                    "description": "Found dead from a gunshot wound to the chest"
                },
                "weapon": {
                    "type": "Pistol",
                    "description": "A .38 caliber pistol was found next to the body. It had been recently fired and contained the victim's fingerprints."
                },
                "suspects": [
                    {
                        "name": "Margaret Blackwood",
                        "age": 52,
                        "occupation": "Housewife",
                        "relationship": "Wife of victim",
                        "alibi": "Claims she was in the garden when she heard the gunshot",
                        "motive": "Stands to inherit significant wealth"
                    },
                    {
                        "name": "David Blackwood",
                        "age": 28,
                        "occupation": "Unemployed",
                        "relationship": "Son of victim",
                        "alibi": "Says he was in his room playing video games",
                        "motive": "Recently cut off from father's money due to gambling debts"
                    },
                    {
                        "name": "Sarah Chen",
                        "age": 34,
                        "occupation": "Secretary",
                        "relationship": "Employee and rumored affair",
                        "alibi": "Claims she was organizing files in the office",
                        "motive": "Victim threatened to fire her after ending their affair"
                    }
                ],
                "evidence": [
                    "Pistol with victim's fingerprints",
                    "Locked door with key in victim's pocket",
                    "Open window in the study",
                    "Muddy footprints under the window"
                ],
                "killer": "sarah chen",
                "solution": {
                    "killer": "Sarah Chen",
                    "motive": "Victor ended their affair and threatened to fire her",
                    "method": "Shot through the open window, then climbed in to place the gun and lock the door from inside before escaping through the window again",
                    "key_evidence": "Muddy footprints under the window matched Sarah's shoes"
                },
                "time_of_death": "3:30 PM",
                "scene_description": "The study was in perfect order except for the body and the open window",
                "motive_hint": "Look for someone with both access and a reason to want Victor dead"
            },
            {
                "id": 2,
                "title": "Death at the Dinner Party",
                "description": "A guest dies from poisoning during an elegant dinner party",
                "difficulty": "Hard",
                "time_limit": 600,  # 10 minutes
                "location": "Riverside Manor",
                "date": "November 3, 2023",
                "summary": "Dr. Elena Rodriguez collapsed and died during dinner at the Riverside Manor. Toxicology revealed she was poisoned with cyanide. Five other guests were present at the dinner.",
                "victim": {
                    "name": "Dr. Elena Rodriguez",
                    "age": 45,
                    "occupation": "Research Scientist",
                    "description": "Died from cyanide poisoning during dinner"
                },
                "weapon": {
                    "type": "Poison",
                    "description": "Cyanide was found in the victim's wine glass. The poison was administered sometime during the dinner."
                },
                "suspects": [
                    {
                        "name": "James Morrison",
                        "age": 52,
                        "occupation": "Pharmaceutical Executive",
                        "relationship": "Former business partner",
                        "alibi": "Was talking to other guests throughout dinner",
                        "motive": "Elena discovered his company was falsifying drug trial results"
                    },
                    {
                        "name": "Lisa Rodriguez",
                        "age": 38,
                        "occupation": "Lawyer",
                        "relationship": "Estranged sister",
                        "alibi": "Was serving wine to guests",
                        "motive": "Elena inherited their parents' estate, leaving Lisa with nothing"
                    },
                    {
                        "name": "Dr. Michael Foster",
                        "age": 49,
                        "occupation": "Research Scientist",
                        "relationship": "Colleague and rival",
                        "alibi": "Was in the bathroom when Elena collapsed",
                        "motive": "Elena was about to publish research that would discredit his life's work"
                    },
                    {
                        "name": "Catherine Wells",
                        "age": 41,
                        "occupation": "Chef",
                        "relationship": "Host of the dinner party",
                        "alibi": "Was in the kitchen preparing dessert",
                        "motive": "Elena gave her restaurant a scathing review, causing it to close"
                    }
                ],
                "evidence": [
                    "Cyanide in wine glass",
                    "Bottle of cyanide found in kitchen trash",
                    "Elena's phone showing threatening messages",
                    "Fingerprints on the wine bottle"
                ],
                "killer": "lisa rodriguez",
                "solution": {
                    "killer": "Lisa Rodriguez",
                    "motive": "Wanted Elena's inheritance",
                    "method": "Added cyanide to Elena's wine while serving drinks",
                    "key_evidence": "Her fingerprints were on the wine bottle and she had access to cyanide from her ex-husband's lab"
                },
                "time_of_death": "8:45 PM",
                "scene_description": "Elegant dining room with six place settings, one knocked over",
                "motive_hint": "The killer had both opportunity and access to poison"
            },
            {
                "id": 3,
                "title": "The Midnight Intruder",
                "description": "A home invasion turns deadly in the suburbs",
                "difficulty": "Easy",
                "time_limit": 300,  # 5 minutes
                "location": "Suburban Home",
                "date": "September 22, 2023",
                "summary": "Robert Mason was found dead in his home after what appeared to be a burglary. However, nothing valuable was taken, and the evidence suggests the killer knew the victim.",
                "victim": {
                    "name": "Robert Mason",
                    "age": 42,
                    "occupation": "Accountant",
                    "description": "Found dead from blunt force trauma to the head"
                },
                "weapon": {
                    "type": "Baseball bat",
                    "description": "A wooden baseball bat from the victim's own collection was used as the murder weapon."
                },
                "suspects": [
                    {
                        "name": "Jennifer Mason",
                        "age": 39,
                        "occupation": "Nurse",
                        "relationship": "Estranged wife",
                        "alibi": "Claims she was working a night shift at the hospital",
                        "motive": "Bitter divorce proceedings, stood to gain from life insurance"
                    },
                    {
                        "name": "Tommy Rodriguez",
                        "age": 24,
                        "occupation": "Handyman",
                        "relationship": "Neighbor",
                        "alibi": "Says he was home watching TV",
                        "motive": "Robert caught him stealing and threatened to call police"
                    },
                    {
                        "name": "Frank Mason",
                        "age": 67,
                        "occupation": "Retired",
                        "relationship": "Father of victim",
                        "alibi": "Claims he was asleep at home",
                        "motive": "Robert was planning to put him in a nursing home"
                    }
                ],
                "evidence": [
                    "No signs of forced entry",
                    "Victim's wallet and valuables untouched",
                    "Bloody baseball bat from victim's collection",
                    "Muddy footprints leading to back door"
                ],
                "killer": "jennifer mason",
                "solution": {
                    "killer": "Jennifer Mason",
                    "motive": "Wanted life insurance money and to avoid alimony payments",
                    "method": "Used her spare key to enter, killed Robert with his own bat, then staged it as a burglary",
                    "key_evidence": "Hospital records showed she wasn't at work during her claimed shift"
                },
                "time_of_death": "11:30 PM",
                "scene_description": "Living room showed signs of a struggle, but no forced entry",
                "motive_hint": "The killer had easy access to the house and knew where the victim kept his valuables"
            }
        ]
        
        # Add 7 more cases to reach 10 total
        cases.extend([
            {
                "id": 4,
                "title": "The Art Gallery Murder",
                "description": "A famous art dealer found dead among priceless paintings",
                "difficulty": "Medium",
                "time_limit": 420,
                "location": "Metropolitan Art Gallery",
                "date": "December 1, 2023",
                "summary": "Renowned art dealer Marcus Rothschild was found dead in his private gallery. A valuable painting was stolen, but the murder seems personal.",
                "victim": {
                    "name": "Marcus Rothschild",
                    "age": 54,
                    "occupation": "Art Dealer",
                    "description": "Found dead from a stab wound to the back"
                },
                "weapon": {
                    "type": "Letter opener",
                    "description": "An ornate letter opener from the victim's desk was used as the murder weapon."
                },
                "suspects": [
                    {
                        "name": "Vivian Cross",
                        "age": 33,
                        "occupation": "Art Appraiser",
                        "relationship": "Business partner",
                        "alibi": "Claims she was at another gallery opening",
                        "motive": "Marcus was about to expose her fake appraisals"
                    },
                    {
                        "name": "Antonio Silva",
                        "age": 41,
                        "occupation": "Artist",
                        "relationship": "Former client",
                        "alibi": "Says he was in his studio painting",
                        "motive": "Marcus sold his paintings as fakes, ruining his career"
                    },
                    {
                        "name": "Rebecca Rothschild",
                        "age": 29,
                        "occupation": "Art Student",
                        "relationship": "Daughter",
                        "alibi": "Claims she was studying at the library",
                        "motive": "Desperate for inheritance money to pay drug debts"
                    }
                ],
                "evidence": [
                    "Letter opener with fingerprints",
                    "Missing Van Gogh painting",
                    "Security camera footage showing masked figure",
                    "Forged authentication documents"
                ],
                "killer": "vivian cross",
                "solution": {
                    "killer": "Vivian Cross",
                    "motive": "Marcus discovered her fake appraisals and threatened to expose her",
                    "method": "Stabbed him with letter opener during a private meeting",
                    "key_evidence": "Her fingerprints were on the letter opener and she had access to the gallery"
                },
                "time_of_death": "7:15 PM",
                "scene_description": "Private gallery office with paintings worth millions",
                "motive_hint": "The killer had both access and something to hide"
            },
            {
                "id": 5,
                "title": "The Campus Conspiracy",
                "description": "A university professor dies under suspicious circumstances",
                "difficulty": "Hard",
                "time_limit": 540,
                "location": "University Campus",
                "date": "October 8, 2023",
                "summary": "Professor William Hayes was found dead in his office. Initially thought to be a heart attack, autopsy revealed he was poisoned with a rare plant toxin.",
                "victim": {
                    "name": "Professor William Hayes",
                    "age": 61,
                    "occupation": "Biology Professor",
                    "description": "Found dead from plant toxin poisoning"
                },
                "weapon": {
                    "type": "Plant toxin",
                    "description": "Ricin extracted from castor beans was found in his coffee."
                },
                "suspects": [
                    {
                        "name": "Dr. Amanda Foster",
                        "age": 44,
                        "occupation": "Chemistry Professor",
                        "relationship": "Colleague",
                        "alibi": "Claims she was teaching a class",
                        "motive": "William was blocking her tenure application"
                    },
                    {
                        "name": "Kevin Chen",
                        "age": 22,
                        "occupation": "Graduate Student",
                        "relationship": "Student",
                        "alibi": "Says he was in the library",
                        "motive": "William was going to fail him, ending his academic career"
                    },
                    {
                        "name": "Dr. Patricia Hayes",
                        "age": 58,
                        "occupation": "University Administrator",
                        "relationship": "Ex-wife",
                        "alibi": "Claims she was in budget meetings",
                        "motive": "William was remarrying, affecting her alimony payments"
                    }
                ],
                "evidence": [
                    "Ricin in coffee cup",
                    "Castor bean plants in campus greenhouse",
                    "Threatening emails to victim",
                    "Chemistry lab access records"
                ],
                "killer": "dr. amanda foster",
                "solution": {
                    "killer": "Dr. Amanda Foster",
                    "motive": "William was blocking her tenure and having an affair with her husband",
                    "method": "Used her chemistry knowledge to extract ricin and poison his coffee",
                    "key_evidence": "Her lab access records show she was there when the ricin was extracted"
                },
                "time_of_death": "2:20 PM",
                "scene_description": "Cluttered professor's office with books and research papers",
                "motive_hint": "The killer needed both motive and knowledge of chemistry"
            },
            {
                "id": 6,
                "title": "The Wedding Day Tragedy",
                "description": "A bride dies on her wedding day",
                "difficulty": "Medium",
                "time_limit": 480,
                "location": "Seaside Wedding Venue",
                "date": "August 14, 2023",
                "summary": "Bride Sarah Williams collapsed and died during her wedding reception. The cause was determined to be a severe allergic reaction, but someone deliberately triggered it.",
                "victim": {
                    "name": "Sarah Williams",
                    "age": 26,
                    "occupation": "Marketing Manager",
                    "description": "Died from severe allergic reaction to peanuts"
                },
                "weapon": {
                    "type": "Peanut oil",
                    "description": "Peanut oil was secretly added to the wedding cake, triggering a fatal allergic reaction."
                },
                "suspects": [
                    {
                        "name": "Emily Johnson",
                        "age": 28,
                        "occupation": "Maid of Honor",
                        "relationship": "Best friend",
                        "alibi": "Was giving a speech when Sarah collapsed",
                        "motive": "Sarah stole her boyfriend years ago"
                    },
                    {
                        "name": "Carol Williams",
                        "age": 52,
                        "occupation": "Real Estate Agent",
                        "relationship": "Mother-in-law",
                        "alibi": "Was mingling with guests",
                        "motive": "Thought Sarah wasn't good enough for her son"
                    },
                    {
                        "name": "chef Maria Santos",
                        "age": 36,
                        "occupation": "Wedding Caterer",
                        "relationship": "Hired help",
                        "alibi": "Was serving other guests",
                        "motive": "Sarah gave her catering business bad reviews"
                    }
                ],
                "evidence": [
                    "Peanut oil in cake frosting",
                    "Sarah's EpiPen was tampered with",
                    "Guest list showing who knew about allergy",
                    "Kitchen access log"
                ],
                "killer": "emily johnson",
                "solution": {
                    "killer": "Emily Johnson",
                    "motive": "Jealousy over Sarah's happiness and old grudges",
                    "method": "Added peanut oil to cake and disabled Sarah's EpiPen",
                    "key_evidence": "She was the only one who knew Sarah's allergy AND had access to her purse"
                },
                "time_of_death": "6:45 PM",
                "scene_description": "Beautiful seaside venue with 150 wedding guests",
                "motive_hint": "The killer knew about Sarah's allergy and had access to her emergency medication"
            },
            {
                "id": 7,
                "title": "The Boardroom Betrayal",
                "description": "A CEO murdered during a hostile takeover",
                "difficulty": "Hard",
                "time_limit": 600,
                "location": "Corporate Headquarters",
                "date": "November 20, 2023",
                "summary": "CEO Jonathan Sterling was found dead in the boardroom after a contentious board meeting. The murder weapon was a trophy from his own shelf.",
                "victim": {
                    "name": "Jonathan Sterling",
                    "age": 48,
                    "occupation": "CEO",
                    "description": "Found dead from blunt force trauma to the head"
                },
                "weapon": {
                    "type": "Crystal trophy",
                    "description": "A heavy crystal award from the victim's achievement shelf was used as the murder weapon."
                },
                "suspects": [
                    {
                        "name": "Diana Foster",
                        "age": 45,
                        "occupation": "CFO",
                        "relationship": "Second in command",
                        "alibi": "Claims she left immediately after the meeting",
                        "motive": "Was being forced out in the hostile takeover"
                    },
                    {
                        "name": "Richard Blake",
                        "age": 55,
                        "occupation": "Board Member",
                        "relationship": "Investor",
                        "alibi": "Says he was on a conference call",
                        "motive": "Jonathan was blocking his takeover bid"
                    },
                    {
                        "name": "Sandra Sterling",
                        "age": 43,
                        "occupation": "Art Gallery Owner",
                        "relationship": "Estranged wife",
                        "alibi": "Claims she was at her gallery",
                        "motive": "Bitter divorce, wanted to prevent asset division"
                    }
                ],
                "evidence": [
                    "Crystal trophy with blood",
                    "Security footage of people leaving building",
                    "Boardroom meeting minutes",
                    "Threatening voicemails"
                ],
                "killer": "richard blake",
                "solution": {
                    "killer": "Richard Blake",
                    "motive": "Jonathan was successfully fighting off his hostile takeover",
                    "method": "Returned to boardroom after meeting and killed Jonathan with trophy",
                    "key_evidence": "Security footage showed he never left the building despite his alibi"
                },
                "time_of_death": "8:30 PM",
                "scene_description": "Corporate boardroom with large table and city view",
                "motive_hint": "The killer had millions at stake in the takeover"
            },
            {
                "id": 8,
                "title": "The Lighthouse Keeper's Secret",
                "description": "A murder at a remote lighthouse",
                "difficulty": "Easy",
                "time_limit": 360,
                "location": "Rocky Point Lighthouse",
                "date": "September 5, 2023",
                "summary": "Lighthouse keeper Henry Walsh was found dead at the bottom of the lighthouse stairs. What appeared to be an accident was actually murder.",
                "victim": {
                    "name": "Henry Walsh",
                    "age": 66,
                    "occupation": "Lighthouse Keeper",
                    "description": "Found dead from injuries after falling down lighthouse stairs"
                },
                "weapon": {
                    "type": "Push",
                    "description": "Victim was pushed down the spiral staircase of the lighthouse."
                },
                "suspects": [
                    {
                        "name": "Beth Walsh",
                        "age": 62,
                        "occupation": "Retired Teacher",
                        "relationship": "Wife",
                        "alibi": "Claims she was shopping in town",
                        "motive": "Henry was planning to leave her for another woman"
                    },
                    {
                        "name": "Danny Morrison",
                        "age": 34,
                        "occupation": "Fisherman",
                        "relationship": "Neighbor",
                        "alibi": "Says he was fixing his boat",
                        "motive": "Henry caught him smuggling drugs using the lighthouse"
                    },
                    {
                        "name": "Mary Walsh",
                        "age": 40,
                        "occupation": "Nurse",
                        "relationship": "Daughter",
                        "alibi": "Claims she was at work",
                        "motive": "Henry was changing his will to leave everything to charity"
                    }
                ],
                "evidence": [
                    "No defensive wounds on victim",
                    "Footprints on lighthouse stairs",
                    "Lighthouse logbook with strange entries",
                    "Hidden compartment with drugs"
                ],
                "killer": "danny morrison",
                "solution": {
                    "killer": "Danny Morrison",
                    "motive": "Henry discovered his drug smuggling operation",
                    "method": "Pushed Henry down the lighthouse stairs during a confrontation",
                    "key_evidence": "His boat was found with drugs and his footprints matched those on the stairs"
                },
                "time_of_death": "4:15 PM",
                "scene_description": "Remote lighthouse with spiral staircase and ocean view",
                "motive_hint": "The killer was using the lighthouse for illegal activities"
            },
            {
                "id": 9,
                "title": "The Charity Gala Murder",
                "description": "Death strikes at a glamorous fundraising event",
                "difficulty": "Medium",
                "time_limit": 450,
                "location": "Grand Ballroom",
                "date": "December 15, 2023",
                "summary": "Philanthropist Grace Montgomery was found dead in the coat check room during a charity gala. Despite the crowd, someone managed to murder her undetected.",
                "victim": {
                    "name": "Grace Montgomery",
                    "age": 54,
                    "occupation": "Philanthropist",
                    "description": "Found dead from strangulation with her own pearl necklace"
                },
                "weapon": {
                    "type": "Pearl necklace",
                    "description": "The victim's expensive pearl necklace was used to strangle her."
                },
                "suspects": [
                    {
                        "name": "Theodore Banks",
                        "age": 59,
                        "occupation": "Charity Director",
                        "relationship": "Business partner",
                        "alibi": "Claims he was giving a speech",
                        "motive": "Grace discovered he was embezzling charity funds"
                    },
                    {
                        "name": "Sophia Montgomery",
                        "age": 31,
                        "occupation": "Fashion Designer",
                        "relationship": "Stepdaughter",
                        "alibi": "Says she was networking with clients",
                        "motive": "Grace was cutting off her trust fund"
                    },
                    {
                        "name": "Martin Cross",
                        "age": 46,
                        "occupation": "Investment Banker",
                        "relationship": "Ex-husband",
                        "alibi": "Claims he was bidding on auction items",
                        "motive": "Grace was exposing his insider trading"
                    }
                ],
                "evidence": [
                    "Pearl necklace around victim's neck",
                    "Torn fabric from expensive dress",
                    "Security footage of coat check area",
                    "Charity financial records"
                ],
                "killer": "theodore banks",
                "solution": {
                    "killer": "Theodore Banks",
                    "motive": "Grace discovered his embezzlement and threatened to expose him",
                    "method": "Lured Grace to coat check room and strangled her with her necklace",
                    "key_evidence": "Fabric from his tuxedo was found under Grace's fingernails"
                },
                "time_of_death": "9:20 PM",
                "scene_description": "Elegant ballroom with 200 guests in formal attire",
                "motive_hint": "The killer had access to charity funds and was desperate to cover up financial crimes"
            },
            {
                "id": 10,
                "title": "The Final Exam",
                "description": "A student dies during finals week",
                "difficulty": "Hard",
                "time_limit": 540,
                "location": "University Library",
                "date": "December 8, 2023",
                "summary": "Top student Rachel Kim was found dead in the library during finals week. Her death was caused by a lethal injection disguised as her diabetes medication.",
                "victim": {
                    "name": "Rachel Kim",
                    "age": 20,
                    "occupation": "Pre-med Student",
                    "description": "Found dead from lethal injection of insulin overdose"
                },
                "weapon": {
                    "type": "Insulin overdose",
                    "description": "A massive insulin overdose was injected using the victim's own insulin pen."
                },
                "suspects": [
                    {
                        "name": "Marcus Thompson",
                        "age": 21,
                        "occupation": "Pre-med Student",
                        "relationship": "Study group member",
                        "alibi": "Claims he was studying in another section",
                        "motive": "Rachel was ruining the grading curve for everyone"
                    },
                    {
                        "name": "Dr. Lisa Chen",
                        "age": 39,
                        "occupation": "Professor",
                        "relationship": "Academic advisor",
                        "alibi": "Says she was grading papers in her office",
                        "motive": "Rachel discovered she was selling test answers"
                    },
                    {
                        "name": "Jake Wilson",
                        "age": 22,
                        "occupation": "Chemistry Student",
                        "relationship": "Ex-boyfriend",
                        "alibi": "Claims he was in the chemistry lab",
                        "motive": "Rachel was going to report him for academic dishonesty"
                    }
                ],
                "evidence": [
                    "Insulin pen with altered dosage",
                    "Library security footage",
                    "Text messages between suspects",
                    "Academic dishonesty reports"
                ],
                "killer": "dr. lisa chen",
                "solution": {
                    "killer": "Dr. Lisa Chen",
                    "motive": "Rachel discovered she was selling test answers and threatened to report her",
                    "method": "Altered Rachel's insulin pen to deliver a lethal dose",
                    "key_evidence": "Her office key was used to access the medical supplies needed to alter the insulin"
                },
                "time_of_death": "11:45 PM",
                "scene_description": "Quiet library study area with individual desks",
                "motive_hint": "The killer had medical knowledge and access to alter the insulin dosage"
            }
        ])
        
        return cases
    
    def get_all_cases(self) -> List[Dict]:
        """Get all available cases"""
        return self.cases
    
    def get_case(self, case_id: int) -> Optional[Dict]:
        """Get a specific case by ID"""
        for case in self.cases:
            if case['id'] == case_id:
                return case
        return None
