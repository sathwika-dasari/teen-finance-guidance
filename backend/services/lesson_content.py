LESSON_DATA = {

"intro_finance": {
    "title": "Basics of Finance",
    "image": "../assets/intro_finance.png",

    "topics": [

        {
            "title": "What is Finance?",
            "content": """Finance refers to the management of money and financial resources. 
It involves activities such as saving, budgeting, investing, and spending wisely. 
Every individual deals with finance in daily life when making decisions about how money is used. 
Understanding finance helps people plan their future, avoid unnecessary debt, and achieve financial stability. 
Learning financial concepts early helps individuals develop responsible money habits."""
        },

        {
            "title": "Importance of Financial Literacy",
            "content": """Financial literacy means understanding how money works in everyday life. 
People who are financially literate can make better decisions about spending and saving. 
They are able to avoid scams, manage debts, and invest money wisely. 
Financial literacy also helps people plan for long-term goals such as education, buying a home, or retirement. 
Developing financial knowledge improves confidence when making financial decisions."""
        },

        {
            "title": "Saving Money",
            "content": """Saving money is an important financial habit that helps individuals prepare for the future. 
Savings can be used for emergencies such as medical expenses or unexpected financial problems. 
Many financial experts recommend saving a portion of income regularly. 
Even small savings grow over time when practiced consistently. 
Developing the habit of saving early helps build financial security."""
        },

        {
            "title": "Spending Wisely",
            "content": """Spending wisely means making careful decisions about how money is used. 
People should learn to distinguish between needs and wants before spending. 
Needs include essential things such as food, education, and housing, while wants include entertainment and luxury items. 
Controlling unnecessary spending helps increase savings and prevents financial stress. 
Responsible spending habits lead to better financial health."""
        }

    ],

    "quiz": [
        {"q": "What does finance mainly deal with?", "a": ["Managing money", "Playing games", "Cooking food"], "correct": 0},
        {"q": "Why is saving money important?", "a": ["For emergencies and future goals", "To waste money", "To hide money"], "correct": 0},
        {"q": "What is financial literacy?", "a": ["Knowledge about managing money", "Watching movies", "Ignoring money"], "correct": 0}
    ]
},

"scam_prevention": {
    "title": "Scam Prevention",
    "image": "../assets/scam_prevention.png",
    "scam_game": [
        {
            "id": 1,
            "type": "Email",
            "image": "https://i.imgur.com/8kQzQ9v.png",
            "scenario": "You receive this email: 'Dear User, Your bank account has been suspended. Click here immediately to verify your details and restore access: www.secure-bank-verify.xyz'",
            "is_scam": True,
            "explanation": "🚨 This is a PHISHING SCAM! Real banks never ask you to click suspicious links. The URL 'www.secure-bank-verify.xyz' is not an official bank website. Always go directly to your bank's official website."
        },
        {
            "id": 2,
            "type": "WhatsApp Message",
            "image": "https://i.imgur.com/placeholder.png",
            "scenario": "WhatsApp message: 'Congratulations! You have won ₹50,000 in our lucky draw! Send ₹500 registration fee to claim your prize. Limited time offer!'",
            "is_scam": True,
            "explanation": "🚨 This is a PRIZE SCAM! Legitimate contests never ask you to pay money to claim winnings. If you have to pay to receive a prize, it's always a scam."
        },
        {
            "id": 3,
            "type": "Investment Offer",
            "image": "https://i.imgur.com/placeholder2.png",
            "scenario": "Instagram ad: 'Invest ₹1000 today and get ₹10,000 back in 7 days! 1000% guaranteed returns! Join 50,000 happy investors!'",
            "is_scam": True,
            "explanation": "🚨 This is a FAKE INVESTMENT SCAM! No legitimate investment guarantees 1000% returns in 7 days. Real investments involve risk and grow slowly over time."
        },
        {
            "id": 4,
            "type": "Job Offer",
            "image": "https://i.imgur.com/placeholder3.png",
            "scenario": "Email from jobs@amazon-hiring.in: 'Amazon is hiring work-from-home employees. Salary ₹50,000/month. No experience needed. Pay ₹2000 registration fee to get started.'",
            "is_scam": True,
            "explanation": "🚨 This is a FAKE JOB SCAM! Legitimate companies never charge a registration fee for employment. Also notice the email is from 'amazon-hiring.in' not the official 'amazon.com'."
        },
        {
            "id": 5,
            "type": "OTP Request",
            "image": "https://i.imgur.com/placeholder4.png",
            "scenario": "Phone call: 'Hello, I am calling from SBI Bank. We detected suspicious activity on your account. Please share the OTP you just received to secure your account.'",
            "is_scam": True,
            "explanation": "🚨 This is a VISHING SCAM! Banks NEVER ask for OTPs over the phone. OTPs are private and should never be shared with anyone, even someone claiming to be from your bank."
        }
    ],

    "topics": [

        {
            "title": "Understanding Online Scams",
            "content": """Online scams are fraudulent activities designed to trick people into giving away money or personal information. 
Scammers often pretend to be trusted companies or financial institutions. 
They may create fake emails, messages, or websites that appear legitimate. 
Once victims trust them, scammers steal sensitive information such as passwords or bank details. 
Being aware of these scams is the first step to protecting yourself."""
        },

        {
            "title": "Phishing Attacks",
            "content": """Phishing is one of the most common online scams. 
In phishing attacks, scammers send emails or messages pretending to be from banks, social media platforms, or companies. 
These messages often include links that lead to fake websites. 
When users enter their login details on these fake sites, scammers collect their information. 
Always check website URLs carefully before entering personal details."""
        },

        {
            "title": "Fake Investment Schemes",
            "content": """Some scammers attract people by promising extremely high returns on investments. 
They claim that their investment opportunity will double or triple money quickly. 
However, most of these schemes are fake and only designed to steal money from victims. 
Real investments always involve some risk and rarely guarantee huge profits instantly. 
It is important to research before investing money anywhere."""
        },

        {
            "title": "How to Stay Safe Online",
            "content": """Protecting yourself online requires awareness and careful behavior. 
Never share passwords, banking details, or private keys with anyone. 
Always verify the authenticity of emails and websites before trusting them. 
Use strong passwords and enable two-factor authentication whenever possible. 
If an offer sounds too good to be true, it is probably a scam."""
        }

    ],

    "quiz": [
        {"q": "What is phishing?", "a": ["Fake messages or websites used to steal information", "Fishing hobby", "Banking service"], "correct": 0, "explanation": "Phishing is a method where scammers try to trick you into revealing sensitive info like passwords or credit card numbers."},
        {"q": "What should you do if someone asks for your password?", "a": ["Share it", "Never share it", "Send it later"], "correct": 1, "explanation": "Your password is your private key to your accounts. Legitimate companies will never ask for it."},
        {"q": "What is a common sign of a scam investment?", "a": ["Guaranteed huge profits", "Long research process", "Low risk"], "correct": 0, "explanation": "If it sounds too good to be true, it probably is. No legitimate investment can guarantee massive, risk-free profits."}
    ]
},

"budgeting_101": {
    "title": "Introduction to Budgeting",
    "image": "../assets/budgeting_101.png",

    "topics": [

        {
            "title": "Understanding Budgeting",
            "content": """Budgeting is the process of creating a structured plan for how money will be spent and saved over a period of time. 
It helps individuals organize their finances and avoid unnecessary spending. 
A budget allows people to understand their financial situation clearly by comparing income and expenses. 
When people follow a budget, they can make better financial decisions and avoid financial stress. 
Budgeting is not about restricting spending but about spending wisely. 
It ensures that essential expenses such as food, education, and transportation are covered. 
It also allows people to allocate money for savings and future goals. 
Budgeting helps develop financial discipline and responsibility. 
Over time, it becomes a powerful tool for building financial security. 
Learning budgeting early helps teenagers develop strong money management habits."""
        },

        {
            "title": "Tracking Your Expenses",
            "content": """Tracking expenses means keeping a record of where money is spent on a daily or monthly basis. 
Many people are unaware of how much money they spend on small purchases. 
Recording expenses helps individuals understand their spending patterns. 
It allows them to identify areas where money might be wasted. 
For example, frequent spending on snacks or entertainment can add up quickly. 
By tracking expenses, individuals can control unnecessary spending. 
Expense tracking also helps when creating a realistic budget. 
People can use notebooks, spreadsheets, or mobile apps to track expenses. 
Regularly reviewing spending habits helps improve financial decisions. 
This practice encourages responsible financial behavior."""
        },

        {
            "title": "Needs vs Wants",
            "content": """A key concept in budgeting is understanding the difference between needs and wants. 
Needs are essential things required for survival and daily living. 
These include food, education, housing, and healthcare. 
Wants are things that improve comfort but are not essential for survival. 
Examples of wants include expensive gadgets, luxury clothes, and entertainment. 
Budgeting requires prioritizing needs before spending money on wants. 
This helps prevent financial problems and unnecessary debt. 
Learning to control impulse spending is an important skill. 
Making thoughtful decisions about wants helps maintain financial balance. 
Understanding this difference leads to smarter financial choices."""
        },

        {
            "title": "Saving Through Budgeting",
            "content": """Saving money is one of the most important goals of budgeting. 
A well-planned budget ensures that a portion of income is always set aside for savings. 
Savings help individuals prepare for emergencies such as medical expenses or unexpected problems. 
They also support long-term goals like education, travel, or starting a business. 
Even small savings can grow significantly over time. 
Consistent saving builds financial security and independence. 
Many experts recommend saving at least a small percentage of income regularly. 
Budgeting makes saving a priority instead of an afterthought. 
This habit helps individuals feel more confident about their financial future. 
Over time, savings can help people achieve important life goals."""
        }

    ],

    "quiz": [
        {"q": "What is budgeting?", "a": ["A plan for managing money", "A type of game", "A loan system"], "correct": 0, "explanation": "Budgeting is simply a plan for every rupee you earn and spend."},
        {"q": "Why track expenses?", "a": ["To understand spending habits", "To waste time", "To increase spending"], "correct": 0, "explanation": "Tracking shows you exactly where your money is going, helping you cut down on 'leakage'."},
        {"q": "What are needs?", "a": ["Essential things for survival", "Luxury items", "Entertainment"], "correct": 0, "explanation": "Needs are things you can't live without, like food and shelter."}
    ]
},

"investing_stocks": {
    "title": "Investing in Stocks",
    "image": "../assets/investing_stocks.png",

    "topics": [

        {
            "title": "What Are Stocks?",
            "content": """Stocks represent ownership in a company. 
When people buy stocks, they become partial owners of that company. 
If the company grows and becomes successful, the value of the stock usually increases."""
        },

        {
            "title": "How Investors Make Money",
            "content": """Investors make money from stocks mainly in two ways. 
First, they can sell stocks at a higher price than they purchased them for. 
Second, companies sometimes pay dividends."""
        }

    ],

    "quiz": [
        {"q": "What does owning a stock mean?", "a": ["Owning part of a company", "Loan to bank", "Free product"], "correct": 0, "explanation": "A stock is essentially a tiny piece of a company. You're an owner!"},
        {"q": "What is a dividend?", "a": ["Company profit shared with investors", "Tax payment", "Loan repayment"], "correct": 0, "explanation": "Dividends are payments made by a corporation to its shareholders out of its profits."}
    ]
},

"advanced_budgeting": {
"title": "Mastering Budgeting",
"image": "../assets/budgeting_101.png",

"topics":[

{
"title":"Strategic Budget Planning",
"content":"""Advanced budgeting focuses on planning finances in a strategic and organized way. 
Instead of simply recording expenses, individuals analyze their financial habits carefully. 
This helps them understand where money is being used effectively. 
Strategic budgeting allows people to align spending with their long-term goals. 
For example, someone saving for education may reduce unnecessary expenses. 
Budgeting also helps create better financial priorities. 
A strategic plan helps balance spending, saving, and investing. 
It encourages individuals to think about future financial needs. 
People who use strategic budgeting often experience greater financial stability. 
Over time, it helps individuals build wealth and achieve financial independence."""
},

{
"title":"The 50-30-20 Budget Rule",
"content":"""The 50-30-20 rule is one of the most popular budgeting strategies. 
It divides income into three main categories. 
Fifty percent of income is used for needs such as housing, food, and transportation. 
Thirty percent is allocated for wants like entertainment and hobbies. 
Twenty percent is dedicated to savings and investments. 
This rule helps individuals maintain a balanced financial lifestyle. 
It ensures that essential expenses are covered first. 
It also encourages consistent saving habits. 
Many financial experts recommend this rule for beginners. 
It provides a simple yet effective approach to financial planning."""
},

{
"title":"Emergency Funds",
"content":"""An emergency fund is a reserve of money set aside for unexpected situations. 
These situations may include medical emergencies, job loss, or urgent repairs. 
Financial experts recommend saving enough money to cover several months of expenses. 
Having an emergency fund provides financial security during difficult times. 
It prevents individuals from relying on loans or credit cards. 
Emergency savings reduce financial stress and anxiety. 
They also provide flexibility when facing unexpected challenges. 
Building an emergency fund takes time and discipline. 
Regular contributions to savings make it possible to build this fund. 
This financial cushion is essential for long-term stability."""
},

{
"title":"Budgeting for Wealth Building",
"content":"""Advanced budgeting also focuses on building wealth over time. 
Instead of only managing expenses, individuals start investing money. 
Investments help grow savings through interest, dividends, or market growth. 
Budgeting allows individuals to allocate money specifically for investments. 
This may include stocks, mutual funds, or retirement plans. 
Consistent investing over many years can significantly increase wealth. 
Budgeting ensures that investments are made regularly. 
It helps maintain financial discipline even during market fluctuations. 
Over time, this strategy supports long-term financial independence. 
Wealth building requires patience, planning, and responsible budgeting."""
}

],

"quiz":[
{"q":"What does the 20% in the 50-30-20 rule represent?","a":["Savings and investments","Entertainment","Food"],"correct":0, "explanation": "The last 20% of your income should go toward financial goals: debt payoff and savings."},
{"q":"What is an emergency fund used for?","a":["Unexpected expenses","Shopping","Entertainment"],"correct":0, "explanation": "An emergency fund is for true surprises, like a medical bill or a broken phone."}
]
},

"taxation_basics": {
"title":"Adulting: Tax and Finance",
"image":"../assets/intro_finance.png",

"topics":[

{
"title":"Understanding Taxes",
"content":"""Taxes are mandatory payments that individuals and businesses make to the government. 
These payments are used to fund important public services. 
Governments use tax revenue to build roads, maintain hospitals, and support education systems. 
Taxes also help provide security services such as police and defense. 
Without taxes, governments would not be able to operate efficiently. 
Different countries have different tax systems. 
Understanding taxes helps individuals manage their financial responsibilities. 
Citizens who pay taxes contribute to the development of their society. 
Learning about taxes is an important part of financial literacy. 
Responsible taxpayers help strengthen national economies."""
},

{
"title":"Types of Taxes",
"content":"""There are several types of taxes that individuals may encounter. 
Income tax is paid on money earned through salaries or businesses. 
Sales tax is added when people purchase goods and services. 
Property tax is paid by individuals who own land or buildings. 
Some countries also collect capital gains tax from investments. 
Each tax serves a different purpose in supporting government operations. 
Understanding different tax types helps individuals plan finances better. 
It also helps people avoid legal or financial problems. 
Governments use tax systems to manage economic growth. 
Knowing about taxes helps citizens make informed financial decisions."""
},

{
"title":"Why Paying Taxes Matters",
"content":"""Paying taxes is an important responsibility for every citizen. 
Taxes support the development of public infrastructure such as roads and bridges. 
They also fund hospitals, schools, and welfare programs. 
Taxes help governments provide services that benefit society as a whole. 
When citizens pay taxes honestly, the economy becomes stronger. 
Avoiding taxes can lead to legal consequences and penalties. 
Responsible taxpayers contribute to national development. 
Tax revenue also helps governments respond to emergencies and disasters. 
Understanding the importance of taxes encourages responsible citizenship. 
Financial awareness helps individuals meet their tax obligations properly."""
},

{
"title":"Basic Tax Planning",
"content":"""Tax planning involves organizing finances in a way that minimizes tax liability legally. 
Individuals can plan investments and savings to reduce taxable income. 
Many governments provide tax benefits for education, healthcare, and retirement savings. 
Understanding these benefits helps people manage finances more effectively. 
Tax planning should always follow legal guidelines and regulations. 
Professional financial advisors often help individuals with tax planning strategies. 
Proper planning prevents financial stress during tax season. 
It also ensures that individuals do not overpay taxes unnecessarily. 
Tax planning is an important part of responsible financial management. 
Learning these skills helps individuals build long-term financial stability."""
}

],

"quiz":[
{"q":"What are taxes used for?","a":["Funding public services","Personal savings","Entertainment"],"correct":0, "explanation": "Taxes pay for things we all use, like roads, hospitals, and schools."}
]
},

"freelance_dev_lesson": {
    "title": "Intro to Freelance Web Dev",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "The Tech Stack", "content": "A successful freelance web developer needs a strong foundation in HTML, CSS, and JavaScript. These languages form the building blocks of the web. As you advance, learning a frontend framework like React or Vue will allow you to build complex web applications faster."},
        {"title": "Building a Portfolio", "content": "Your portfolio is your resume. Start by building 3-5 high-quality projects. Add a personal website, a landing page for a fictional business, and an interactive web app. Host your code on GitHub and deploy your sites using free services like Netlify or Vercel."},
        {"title": "Landing Your First Client", "content": "Finding clients takes persistence. Start by setting up profiles on freelance marketplaces like Upwork, Fiverr, or Freelancer. Alternatively, reach out to local businesses (like restaurants or gyms) that have outdated websites. Offer them a discounted rate for your first project."}
    ],
    "quiz": [
        {"q": "What is the most important asset for a freelance developer?", "a": ["A strong portfolio", "An expensive laptop", "A business suit"], "correct": 0, "explanation": "Clients want to see what you've built. Portfolios prove your skills."},
        {"q": "Where can you host your web projects for free?", "a": ["GitHub and Netlify", "Microsoft Word", "Your local hard drive"], "correct": 0, "explanation": "Many modern platforms offer free hosting for developer projects."}
    ]
},

"graphic_design_lesson": {
    "title": "Starting in Graphic Design",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "Mastering the Tools", "content": "Graphic design requires mastering tools like Adobe Illustrator, Photoshop, or free alternatives like Figma and Canva. Start by learning the basics of vector graphics, layers, and typography. Practice recreating popular logos and flyers to understand the techniques professionals use."},
        {"title": "Design Principles", "content": "Great design is built on fundamental principles: contrast, repetition, alignment, and proximity. Understanding color theory and how to choose complementary colors is crucial. Typography also plays a massive role—knowing when to use a serif vs. sans-serif font can make or break a design."},
        {"title": "Showcasing Your Art", "content": "Create a visual portfolio on platforms like Behance, Dribbble, or Instagram. Post your work consistently and engage with other designers. When pitching to clients, tailor your portfolio to show designs relevant to their industry (e.g., modern logos for tech startups)."}
    ],
    "quiz": [
        {"q": "Which of these is a fundamental design principle?", "a": ["Alignment", "Typing speed", "File size"], "correct": 0, "explanation": "Alignment helps create a sense of order and structure in a design."},
        {"q": "Which tool is commonly used by UI/UX designers?", "a": ["Figma", "Excel", "Notepad"], "correct": 0, "explanation": "Figma is a collaborative interface design tool widely used in tech."}
    ]
},

"content_writing_lesson": {
    "title": "Becoming a Content Writer",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "Finding Your Niche", "content": "Content writing covers everything from blog posts to technical manuals. The key to earning higher rates is finding a niche you are passionate about, such as technology, finance, health, or lifestyle. Niche writers are seen as experts and are highly valued by businesses."},
        {"title": "The Art of Copywriting", "content": "While content writing aims to educate, copywriting aims to sell. Learning the basics of persuasive writing and SEO (Search Engine Optimization) will make your work much more valuable. Always write with clarity, keep sentences concise, and structure your posts with clear headings."},
        {"title": "Pitching to Clients", "content": "Start by publishing your writing on platforms like Medium or your own blog to build a portfolio. Join job boards like ProBlogger or pitch directly to editors of digital publications. A good pitch is short, includes your best writing samples, and explains how your article will benefit their specific audience."}
    ],
    "quiz": [
        {"q": "What does SEO stand for?", "a": ["Search Engine Optimization", "Super Effective Organization", "Standard English Output"], "correct": 0, "explanation": "SEO is the practice of increasing the quantity and quality of traffic to your website through organic search engine results."},
        {"q": "Why is finding a niche important?", "a": ["It makes you an expert in a specific field", "It is easier to type", "It costs less"], "correct": 0, "explanation": "Being an expert allows you to charge more and deliver better content."}
    ]
},

"online_tutor_lesson": {
    "title": "Succeeding as an Online Tutor",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "Choosing Your Subjects", "content": "Focus on subjects you excel at, such as high school math, science, coding, or foreign languages. Determine what age group you are most comfortable teaching. Having a specialized focus helps you stand out to parents and students searching for help."},
        {"title": "Creating a Virtual Classroom", "content": "A professional setup is essential for online tutoring. Ensure you have a quiet environment, reliable high-speed internet, a good webcam, and a clear microphone. Familiarize yourself with digital whiteboard tools and video conferencing platforms like Zoom or Google Meet."},
        {"title": "Building Student Loyalty", "content": "Patience and clear communication are key. Prepare lesson plans in advance and track your student's progress. Encourage a positive learning environment by celebrating small victories. A satisfied student often leads to long-term work and referrals to other parents."}
    ],
    "quiz": [
        {"q": "What is essential for an online tutoring setup?", "a": ["A quiet environment and good internet", "Loud music", "A television"], "correct": 0, "explanation": "Clarity is key. Students need to hear and see you without distractions."},
        {"q": "How can you build student loyalty?", "a": ["By tracking progress and showing patience", "By ending sessions early", "By giving them no homework"], "correct": 0, "explanation": "Helping students see their own progress builds trust and confidence."}
    ]
},

"social_media_manager_lesson": {
    "title": "Social Media Management",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "Understanding the Algorithms", "content": "Social Media Managers need to understand how different platforms work. Instagram favors visual aesthetic and Reels, Twitter focuses on timely text interactions, and LinkedIn is for professional networking. Mastering the algorithm of your chosen platforms is your biggest asset."},
        {"title": "Content Calendars and Strategy", "content": "Consistency is key to growth. Use tools like Hootsuite or Buffer to schedule posts in advance using a Content Calendar. A good strategy mixes educational, entertaining, and promotional content. Analyze your engagement metrics to see what type of posts perform best."},
        {"title": "Growing a Brand", "content": "Businesses hire social media managers to grow their audience and drive sales. Focus on community engagement—reply to comments, participate in trends, and collaborate with other creators. Building a loyal community is more valuable than just getting viral views."}
    ],
    "quiz": [
        {"q": "Why is consistency important in social media?", "a": ["It keeps the audience engaged and satisfies algorithms", "It uses up data", "It annoys followers"], "correct": 0, "explanation": "Algorithms reward regular posters, and audiences like predictable schedules."},
        {"q": "What is a Content Calendar used for?", "a": ["Planning and scheduling posts in advance", "Tracking your physical workouts", "Recording expenses"], "correct": 0, "explanation": "Organization prevents last-minute panics and ensures a variety of content."}
    ]
},

"virtual_assistant_lesson": {
    "title": "The Virtual Assistant Path",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "Core VA Skills", "content": "A Virtual Assistant (VA) helps business owners with administrative tasks. Essential skills include extreme organization, clear communication, and time management. You must be comfortable managing emails, scheduling calendar events, and handling customer inquiries remotely."},
        {"title": "Mastering the Software Tools", "content": "Familiarity with modern productivity software is a must. You should master Google Workspace (Docs, Sheets, Drive), project management tools like Trello or Asana, and communication platforms like Slack. Being tech-savvy allows you to integrate seamlessly into a client's business."},
        {"title": "Finding VA Opportunities", "content": "Join Facebook groups specifically for entrepreneurs or VAs where clients frequently post jobs. You can also create profiles on Upwork or Fiverr. Start by offering basic admin packages, and as you gain experience, you can offer premium services like market research or bookkeeping."}
    ],
    "quiz": [
        {"q": "What is a core skill for a Virtual Assistant?", "a": ["Extreme organization", "Physical strength", "Cooking ability"], "correct": 0, "explanation": "Being organized is the #1 job description for a VA. Clients pay for your orderliness."},
        {"q": "Which tools should a VA master?", "a": ["Google Workspace and project management apps", "Video games", "Video editing software"], "correct": 0, "explanation": "VAs must be experts in the 'office' tools of the digital world."}
    ]
},

"saving_money": {
    "title": "Saving Money Strategies",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "The Power of Compound Interest", "content": "Compound interest is when you earn interest on both the money you've saved and the interest you've already earned. The earlier you start saving, the more time compound interest has to work its magic."},
        {"title": "High Yield vs Standard Accounts", "content": "A high-yield savings account offers a significantly higher interest rate than a standard checking account. If you're saving for something more than a few months away, this is where your money should sit."}
    ],
    "quiz": [
        {"q": "What is compound interest?", "a": ["Interest on both original money and accumulated interest", "A type of loan", "A bank fee"], "correct": 0, "explanation": "Einstein called compound interest the 'eighth wonder of the world'."},
        {"q": "Where should you keep long-term savings?", "a": ["High-yield savings account", "Under the mattress", "Regular checking account"], "correct": 0, "explanation": "High-yield accounts keep your money working for you."}
    ]
},

"basic_banking": {
    "title": "Basic Banking",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "Checking vs Savings", "content": "A checking account is for daily transactions like buying food or paying bills. A savings account is for storing money securely to earn interest over time. You should transfer money from checking to savings regularly."},
        {"title": "Hidden Fees", "content": "Banks sometimes charge maintenance fees, overdraft fees, or ATM fees. Always read the terms when opening an account. Look for student or teen accounts that waive these fees."}
    ],
    "quiz": [
        {"q": "What is a checking account primarily used for?", "a": ["Daily transactions and spending", "Earning high interest", "Retirement savings"], "correct": 0, "explanation": "Checking is for 'in and out' money."},
        {"q": "What should you watch out for when opening a bank account?", "a": ["Hidden fees like maintenance and overdrafts", "Free lollipops", "The color of the bank"], "correct": 0, "explanation": "Fees can eat up your balance. Always look for free accounts."}
    ]
},

"digital_payments": {
    "title": "Digital Payments & UPI",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "How UPI Works", "content": "UPI (Unified Payments Interface) allows instant money transfer between bank accounts using a mobile phone. It is fast and typically fee-free, making it the most popular digital payment method today."},
        {"title": "Setting up Secure PINs", "content": "Your UPI PIN is like your ATM PIN. Never share it, not even with the bank. If an app asks you to enter your PIN to 'receive' money, IT IS A SCAM. You only enter pins to SEND money."}
    ],
    "quiz": [
        {"q": "Do you need to enter your UPI PIN to RECEIVE money?", "a": ["No, never. If asked, it's a scam.", "Yes, always.", "Only for large amounts."], "correct": 0, "explanation": "Receiving money is passive. If you have to enter a PIN, you are authorising a *send* transaction."},
        {"q": "What does UPI do?", "a": ["Instant money transfers between bank accounts", "Generates cash", "Prints receipts"], "correct": 0, "explanation": "UPI connects banks directly to your phone for instant payments."}
    ]
},

"understanding_credit": {
    "title": "Understanding Credit",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "What is a Credit Card?", "content": "Unlike a debit card (which uses your own money), a credit card borrows money from the bank. You must pay it back at the end of the month. If you don't, you are charged extremely high interest."},
        {"title": "Credit Scores", "content": "Your credit score is a number that shows banks how reliable you are at paying back debt. Paying your credit card on time builds a good score, making it easier to get cheap loans for cars or houses later in life."}
    ],
    "quiz": [
        {"q": "What happens if you don't pay a credit card bill on time?", "a": ["You get charged high interest and your credit score drops", "Nothing happens", "The bank gives you more money"], "correct": 0, "explanation": "Credit cards are high-interest debt. Always pay in full every month."},
        {"q": "What is a credit score?", "a": ["A number showing how reliable you are with debt", "Your exam grades", "Your follower count"], "correct": 0, "explanation": "Financial institutions use this 'grade' to decide if they should lend to you."}
    ]
},

"side_income": {
    "title": "Side Income Basics",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "What is a Side Hustle?", "content": "A side hustle is a way to make money outside of a primary job or school. Examples include freelancing, selling crafts online, or tutoring. It's a great way to accelerate your savings."},
        {"title": "Time vs Value", "content": "When starting a side hustle, consider if you are trading time for money (like tutoring hourly) or creating value (like selling a digital course that can be bought many times without extra work). Both are valid but scale differently."}
    ],
    "quiz": [
        {"q": "What is a side hustle?", "a": ["Extra work outside primary commitments to make money", "A type of dance", "A banking term"], "correct": 0, "explanation": "It's an additional income stream usually based on your skills or hobbies."},
        {"q": "Which is an example of creating value that scales?", "a": ["Making a digital course once and selling it infinitely", "Walking dogs by the hour", "Mowing lawns"], "correct": 0, "explanation": "Selling a product (digital or physical) doesn't limit you by the hours in a day."}
    ]
},

"mutual_funds": {
    "title": "Mutual Funds",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "What is a Mutual Fund?", "content": "Instead of trying to pick one winning stock, a mutual fund pools money from many investors to buy a massive diversified collection of stocks or bonds. It lowers the risk of losing money if one single company fails."},
        {"title": "SIPs (Systematic Investment Plans)", "content": "An SIP is a method where you invest a fixed, small amount of money into a mutual fund every month instead of one huge amount. It helps balance out the highs and lows of the market over time."}
    ],
    "quiz": [
        {"q": "Why are mutual funds less risky than picking a single stock?", "a": ["Because they are diversified across many companies", "Because the government guarantees them", "Because they don't involve money"], "correct": 0, "explanation": "Diversification spreads your risk. If one company in the fund fails, 99 others are still there."},
        {"q": "What is an SIP?", "a": ["Investing a fixed amount regularly every month", "A quick rich scheme", "A type of debit card"], "correct": 0, "explanation": "SIPs make investing automatic and disciplined."}
    ]
},

"risk_management": {
    "title": "Risk Management",
    "image": "../assets/intro_finance.png",
    "topics": [
        {"title": "The Golden Rule of Risk", "content": "Generally, higher potential returns come with higher risk. If an investment promises you 50% returns in a week with 'no risk', you are being lied to. It's crucial to understand the worst-case scenario before investing."},
        {"title": "Diversification", "content": "Don't put all your eggs in one basket. Risk management means spreading your money across different types of investments (savings accounts, mutual funds, gold) so that if one sector crashes, you don't lose everything."}
    ],
    "quiz": [
        {"q": "What does diversification mean in finance?", "a": ["Spreading money across multiple investments to reduce risk", "Putting all money in one stock", "Hiding money in different rooms"], "correct": 0, "explanation": "Diversification is the most important tool for managing investment risk."},
        {"q": "If an investment promises massive returns with zero risk, what is it likely?", "a": ["A scam or highly misleading", "A safe choice", "A government program"], "correct": 0, "explanation": "High reward ALWAYS comes with high risk. Always."}
    ]
}

}


class LessonService:
    @staticmethod
    def get_lesson_detail(module_id):
        return LESSON_DATA.get(module_id)