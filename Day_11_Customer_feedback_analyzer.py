

'''Your Goal
Write a script that reads these reviews, categorizes them by business department, and flags urgent issues based on the rating.

Your Hints
Hint 1: Create a function called analyze_feedback(rating). 
    Make it return "Needs Attention" if the rating is 3 or below. Make it return "Good Job" if it is 4 or 5.
Hint 2: Use a for loop to iterate through the customer_reviews list.
Hint 3: Inside your loop, check the text strings using the in keyword with if/elif statements. 
        If the text contains words like "chocolate" or "packaging", 
        route it to the US Chocolate team. If it contains "designs", "marketing", or "reels", route it to the S Designs team.
Hint 4: Use f-strings to print a final report for every review. It should show the client, the assigned team, and the status.'''

customer_reviews = [
    {"client": "Pizza Hut", "text": "Great designs, but we need the reels faster.", "rating": 3},
    {"client": "Local Cafe", "text": "The chocolate boxes were perfect for our event!", "rating": 5},
    {"client": "Tech Startup", "text": "Marketing setup is too expensive.", "rating": 2},
    {"client": "Wedding Planner", "text": "Beautiful packaging and fast delivery.", "rating": 5},
    {"client": "Burger Joint", "text": "The social media marketing campaign doubled our weekend sales!", "rating": 5},
    {"client": "Sweet Delights", "text": "We need custom chocolate wrappers for Eid, please reply.", "rating": 4},
    {"client": "Apparel Co", "text": "The logo designs feel outdated. Not happy with the current concepts.", "rating": 2},
    {"client": "Gourmet Bakery", "text": "Amazing luxury packaging. Our clients loved the premium feel.", "rating": 5},
    {"client": "Crypto Wallet", "text": "The promotional reels were way too generic. Need a redo.", "rating": 1},
    {"client": "Hotel Grand", "text": "Marketing strategy was decent, but communication was slow.", "rating": 3},
    {"client": "Candy Land", "text": "The dark chocolate batch was slightly melted upon arrival.", "rating": 2},
    {"client": "Fitness Center", "text": "Great video edits for Instagram reels! Reach is skyrocketing.", "rating": 5},
    {"client": "SaaS Platform", "text": "The landing page designs look extremely clean and professional.", "rating": 5},
    {"client": "Flower Boutique", "text": "Gift packaging was damaged during transit. Fix this.", "rating": 2},
    {"client": "Corporate Gifting Inc", "text": "Bulk chocolate order was processed perfectly and on time.", "rating": 5},
    {"client": "Real Estate Agency", "text": "The Facebook marketing ads aren't bringing in any qualified leads.", "rating": 1},
    {"client": "Auto Shop", "text": "Banner designs are okay, but formatting size is wrong for printing.", "rating": 3},
    {"client": "Coffee House", "text": "White chocolate mocha mix packaging looks stunning.", "rating": 5},
    {"client": "Tech Gadgets", "text": "The launch marketing strategy lacked depth.", "rating": 2},
    {"client": "Clothing Brand", "text": "The fashion reels are highly engaging. Excellent transition edits.", "rating": 5},
    {"client": "Dentist Clinic", "text": "Website UI designs are intuitive and user-friendly.", "rating": 4},
    {"client": "Art Gallery", "text": "Custom premium packaging arrived late. Missed our exhibition opening.", "rating": 1},
    {"client": "Ice Cream Parlor", "text": "Milk chocolate toppings packaging needs a tighter seal.", "rating": 3},
    {"client": "Law Firm", "text": "LinkedIn marketing setup was highly professional and precise.", "rating": 5},
    {"client": "Jewelry Shop", "text": "Brochure designs are elegant but font size is too small to read.", "rating": 3},
    {"client": "Snack Bar", "text": "Assorted chocolate boxes sold out instantly. Need a restock.", "rating": 5},
    {"client": "Consulting Group", "text": "The digital marketing audit was very insightful.", "rating": 4},
    {"client": "Bookstore", "text": "Bookmark designs are creative, but we need more color options.", "rating": 3},
    {"client": "Organic Foods", "text": "Eco-friendly packaging looks raw and matches our brand perfectly.", "rating": 5},
    {"client": "Toy Store", "text": "The animated reels for kids' toys are fun and vibrant.", "rating": 5},
    {"client": "Mobile App", "text": "App Store optimization marketing didn't change our download rate.", "rating": 2},
    {"client": "Boutique Hotel", "text": "Menu designs are clean. Minimalist style suits us.", "rating": 4},
    {"client": "Nut Shop", "text": "Gift boxes and packaging are sturdy. High quality.", "rating": 5},
    {"client": "Perfume House", "text": "The scent collection marketing teaser video looks cinematic.", "rating": 5},
    {"client": "Cafe Bistro", "text": "The customized chocolate favors were a hit with customers.", "rating": 5}
]

def analyze_feedback(rating):
    if rating <= 3:
        return "Needs Attention"
    else:
        return "Good Job"
for i in customer_reviews:
    client = i['client']
    status = analyze_feedback(i['rating'])
    if 'chocolate' in i['text'] or 'packaging' in i['text']:
        team = 'US Chocolate team'
        print(f"Client: {client}, Assigned Team: {team}, Status: {status}")
    elif 'designs' in i['text'] or 'Marketing' in i['text'] or 'Reels' in i['text']:
        team = 'S Designs Team'
        print(f"Client: {client}, Assigned Team: {team}, Status: {status}")

    
    
    

    