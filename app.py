import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Curato | Professional Gifting",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. THE FRONTEND CODE (HTML/CSS/JS)
# ==========================================
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Curato - Professional Gift Concierge</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Poppins (Headings) & Inter (Body) -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <!-- Confetti for the 'Delight' factor -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; }
        h1, h2, h3, .brand-font { font-family: 'Poppins', sans-serif; }
        
        /* Smooth Scroll */
        html { scroll-behavior: smooth; }

        /* Custom Animations */
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-up { animation: fadeUp 0.6s ease-out forwards; }
        
        /* Glassmorphism Card */
        .glass-card {
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.6);
            box-shadow: 0 20px 40px -5px rgba(0, 0, 0, 0.05);
        }

        /* Professional New Year Gradient */
        .text-gradient {
            background: linear-gradient(135deg, #0f172a 0%, #334155 100%); /* Deep Navy/Charcoal */
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Button Press Effect */
        .btn-press:active { transform: scale(0.98); }

        /* Blob Animation */
        @keyframes blob {
            0% { transform: translate(0px, 0px) scale(1); }
            33% { transform: translate(30px, -50px) scale(1.1); }
            66% { transform: translate(-20px, 20px) scale(0.9); }
            100% { transform: translate(0px, 0px) scale(1); }
        }
        .animate-blob {
            animation: blob 10s infinite;
        }
        .animation-delay-2000 {
            animation-delay: 2s;
        }
        
        /* Hide scrollbar for cleaner embed */
        ::-webkit-scrollbar { width: 0px; background: transparent; }
    </style>
</head>
<body class="bg-slate-50 min-h-screen relative overflow-x-hidden selection:bg-slate-200 selection:text-slate-800">

    <!-- Subtle Animated Background -->
    <div class="fixed top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
        <div class="absolute top-[-10%] right-[-5%] w-[600px] h-[600px] bg-blue-50 rounded-full mix-blend-multiply filter blur-3xl opacity-60 animate-blob"></div>
        <div class="absolute top-[20%] left-[-10%] w-[500px] h-[500px] bg-purple-50 rounded-full mix-blend-multiply filter blur-3xl opacity-60 animate-blob animation-delay-2000"></div>
    </div>

    <!-- Navigation / Brand -->
    <nav class="w-full px-6 py-6 flex justify-center">
        <div class="glass-card px-8 py-3 rounded-full flex flex-col items-center cursor-pointer hover:shadow-md transition-all duration-300 group">
            <div class="flex items-center gap-2">
                <span class="text-xl group-hover:rotate-12 transition-transform">🎁</span>
                <span class="font-bold text-slate-800 tracking-tight text-lg">Curato</span>
            </div>
            <span class="text-[10px] text-slate-500 font-medium tracking-widest uppercase mt-1">Professional Concierge</span>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto px-4 py-10 flex flex-col items-center">
        
        <!-- Hero Section -->
        <div class="text-center mb-10 max-w-2xl animate-fade-up">
            <div class="inline-flex items-center gap-2 px-3 py-1 bg-white border border-slate-200 rounded-full text-xs font-bold text-slate-600 mb-6 shadow-sm">
                <span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
                NEW YEAR • FRESH STARTS
            </div>
            <h1 class="text-4xl md:text-5xl font-extrabold mb-6 leading-tight text-slate-900 brand-font">
                A thoughtful start to<br>
                <span class="text-gradient">the new year.</span>
            </h1>
            <p class="text-slate-500 text-lg md:text-xl font-medium leading-relaxed">
                Professional gifting, handled — without the usual confusion or last-minute stress.
            </p>
        </div>

        <!-- The "App" Card -->
        <div class="w-full glass-card rounded-3xl p-6 md:p-10 mb-12 transform transition-all duration-500 hover:shadow-xl animate-fade-up border-t-4 border-slate-800" style="animation-delay: 0.1s;">
            
            <div class="mb-8 border-b border-slate-100 pb-6">
                <h2 class="text-xl font-bold text-slate-800 brand-font">Find the right gift, fast.</h2>
                <p class="text-slate-500 text-sm mt-1">Select the category below.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-10 gap-8 items-start">
                
                <!-- Input 1: Context (Replaced "Who") -->
                <div class="md:col-span-5 relative group">
                    <label class="block text-sm font-bold text-slate-800 mb-1 ml-1">What kind of gift?</label>
                    <p class="text-xs text-slate-400 mb-3 ml-1">We'll filter for professional appropriateness.</p>
                    <div class="relative">
                        <select id="contextInput" class="w-full bg-slate-50 border border-slate-200 text-slate-800 font-medium text-base py-4 px-4 rounded-xl appearance-none focus:outline-none focus:border-slate-800 focus:bg-white transition-colors cursor-pointer shadow-sm">
                            <option value="Desk">Desk Essentials & Stationery</option>
                            <option value="Tech">Tech Gear & Organizers</option>
                            <option value="Travel">Travel & Commute Items</option>
                            <option value="Safe">Safe & Neutral (Universal)</option>
                        </select>
                        <div class="absolute top-4 right-4 flex items-center pointer-events-none text-slate-400">
                            <i data-lucide="chevron-down"></i>
                        </div>
                    </div>
                </div>

                <!-- Input 2: Budget -->
                <div class="md:col-span-3 relative group">
                    <label class="block text-sm font-bold text-slate-800 mb-1 ml-1">Your Budget?</label>
                    <p class="text-xs text-slate-400 mb-3 ml-1">We stick to safe ranges.</p>
                    <div class="relative">
                        <select id="budgetInput" class="w-full bg-slate-50 border border-slate-200 text-slate-800 font-medium text-base py-4 px-4 rounded-xl appearance-none focus:outline-none focus:border-slate-800 focus:bg-white transition-colors cursor-pointer shadow-sm">
                            <option value="500">Under ₹500 (Token)</option>
                            <option value="1500" selected>₹500 – ₹1,500 (Safe)</option>
                            <option value="3000">₹1,500 – ₹3,000 (Special)</option>
                            <option value="10000">Above ₹3,000 (Premium)</option>
                        </select>
                        <div class="absolute top-4 right-4 flex items-center pointer-events-none text-slate-400">
                            <i data-lucide="chevron-down"></i>
                        </div>
                    </div>
                </div>

                <!-- Button -->
                <div class="md:col-span-2 flex flex-col justify-end h-full mt-2">
                    <button onclick="findGifts()" class="btn-press w-full bg-slate-800 hover:bg-slate-900 text-white font-semibold text-base py-4 px-6 rounded-xl shadow-lg shadow-slate-200 transition-all flex items-center justify-center gap-2 group">
                        <span>Shortlist</span>
                        <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                    </button>
                    <p class="text-center text-[10px] text-slate-400 mt-2">Curating top 3 options...</p>
                </div>
            </div>
        </div>

        <!-- Loading State -->
        <div id="loadingState" class="hidden py-12 text-center animate-fade-up">
            <div class="relative w-16 h-16 mx-auto mb-4">
                <div class="absolute top-0 left-0 w-full h-full border-4 border-slate-100 rounded-full"></div>
                <div class="absolute top-0 left-0 w-full h-full border-4 border-slate-800 rounded-full border-t-transparent animate-spin"></div>
            </div>
            <h3 class="text-slate-800 font-semibold text-lg">Reviewing suitable options...</h3>
            <p class="text-slate-400 text-sm mt-1">Checking availability and professional fit.</p>
        </div>

        <!-- Results Grid -->
        <div id="resultsArea" class="hidden w-full animate-fade-up">
            <div class="mb-8 border-l-4 border-slate-800 pl-4 py-1">
                <h2 class="text-2xl font-bold text-slate-900 brand-font">Shortlisted for you</h2>
                <p class="text-slate-500 text-sm mt-1">Practical, appropriate, and ready to buy.</p>
            </div>
            
            <div id="cardsContainer" class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Cards injected via JS -->
            </div>
        </div>

        <!-- Trust Section -->
        <div class="mt-24 border-t border-slate-200 pt-12 w-full max-w-3xl">
            <h3 class="text-center text-slate-800 font-bold text-lg mb-10 brand-font">How we choose gifts for you</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 px-4">
                <div class="text-left group hover:-translate-y-1 transition-transform duration-300">
                    <div class="w-10 h-10 bg-slate-100 rounded-full flex items-center justify-center mb-3 group-hover:bg-slate-200 transition-colors">
                        <i data-lucide="check-circle" class="w-5 h-5 text-green-600"></i>
                    </div>
                    <h4 class="font-bold text-slate-900 text-sm mb-2">High Utility</h4>
                    <p class="text-xs text-slate-500 leading-relaxed">Items that naturally become part of someone’s workday.</p>
                </div>
                <div class="text-left group hover:-translate-y-1 transition-transform duration-300">
                    <div class="w-10 h-10 bg-slate-100 rounded-full flex items-center justify-center mb-3 group-hover:bg-slate-200 transition-colors">
                        <i data-lucide="shield" class="w-5 h-5 text-blue-600"></i>
                    </div>
                    <h4 class="font-bold text-slate-900 text-sm mb-2">Office Safe</h4>
                    <p class="text-xs text-slate-500 leading-relaxed">No novelty items or loud designs. Safe for everyone.</p>
                </div>
                <div class="text-left group hover:-translate-y-1 transition-transform duration-300">
                    <div class="w-10 h-10 bg-slate-100 rounded-full flex items-center justify-center mb-3 group-hover:bg-slate-200 transition-colors">
                        <i data-lucide="tag" class="w-5 h-5 text-purple-600"></i>
                    </div>
                    <h4 class="font-bold text-slate-900 text-sm mb-2">Fair Value</h4>
                    <p class="text-xs text-slate-500 leading-relaxed">Optimized for perceived value within your budget.</p>
                </div>
            </div>
        </div>

    </main>

    <footer class="mt-12 py-8 text-center text-slate-400 text-sm border-t border-slate-100 bg-white">
        <p>&copy; 2025 Curato. Built for Indian workplaces.</p>
    </footer>

    <!-- Logic Script -->
    <script>
        // Initialize Icons
        lucide.createIcons();

        // 1. DATA
        const inventory = [
            // DESK
            { name: "Parker Vector Pen", price: 450, tags: ["safe", "desk", "classic"], url: "https://www.amazon.in/s?k=Parker+Vector+Stainless+Steel+CT+Ball+Pen", pitch: "Selected because it’s universally appropriate, durable, and actually used daily.", bestFor: "Formal settings", imgKeyword: "fountain pen" },
            { name: "Hardcover Journal", price: 499, tags: ["desk", "creative", "safe"], url: "https://www.amazon.in/s?k=Factor+Notes+Hardcover+Notebook+A5", pitch: "Just premium paper. No cheesy quotes or distractions.", bestFor: "Thinkers & planners", imgKeyword: "black notebook" },
            { name: "Alloy Laptop Stand", price: 699, tags: ["tech", "health", "desk"], url: "https://www.amazon.in/s?k=Portronics+My+Buddy+K+Portable+Laptop+Stand", pitch: "High utility. Saves their neck and folds into a stick.", bestFor: "Laptop users", imgKeyword: "laptop stand office" },
            { name: "Vegan Leather Desk Mat", price: 799, tags: ["desk", "setup", "aesthetic"], url: "https://www.amazon.in/s?k=Vegan+Leather+Desk+Mat+Extended", pitch: "Instantly defines a workspace. Makes a messy desk look executive.", bestFor: "New desk setups", imgKeyword: "desk mat" },

            // TECH
            { name: "DailyObjects Tech Kit", price: 1299, tags: ["tech", "travel", "organized"], url: "https://www.amazon.in/s?k=DailyObjects+Tech+Kit+Organizer", pitch: "Fixes the cable mess. Essential for hybrid work.", bestFor: "Hybrid workers", imgKeyword: "tech pouch" },
            { name: "SanDisk Dual Drive", price: 899, tags: ["tech", "utility", "budget"], url: "https://www.amazon.in/s?k=SanDisk+Ultra+Dual+Drive+Go+Type-C", pitch: "High utility choice. Transfers data between phone & laptop instantly.", bestFor: "Tech roles", imgKeyword: "usb flash drive" },
            { name: "Silent Wireless Mouse", price: 599, tags: ["tech", "productivity", "budget"], url: "https://www.flipkart.com/search?q=Portronics+Silent+Mouse", pitch: "The 'Silent Click' is a blessing for open offices.", bestFor: "Open offices", imgKeyword: "computer mouse" },
            { name: "Sleek Laptop Sleeve", price: 999, tags: ["carry", "minimalist", "safe"], url: "https://www.amazon.in/s?k=Vegan+Leather+Laptop+Sleeve+15.6", pitch: "Slim protection that fits inside any backpack.", bestFor: "Commuters", imgKeyword: "laptop sleeve leather" },

            // FUEL
            { name: "Milton Thermosteel", price: 750, tags: ["utility", "travel", "safe"], url: "https://www.amazon.in/s?k=Milton+Thermosteel+Flip+Lid+500ml", pitch: "The gold standard. Keeps coffee hot for 4 hours. Zero leaks.", bestFor: "Daily hydration", imgKeyword: "steel water bottle" },
            { name: "Borosil Glass Lunch Set", price: 950, tags: ["health", "food", "practical"], url: "https://www.amazon.in/s?k=Borosil+Glass+Lunch+Box+Set+of+3", pitch: "Glass feels premium and doesn't stain. Safe for microwaves.", bestFor: "Office lunches", imgKeyword: "glass food container" },
            { name: "Insulated Coffee Mug", price: 1199, tags: ["desk", "coffee", "aesthetic"], url: "https://www.amazon.in/s?k=Insulated+Coffee+Mug+Stainless+Steel", pitch: "Looks better than a generic ceramic mug. Keeps heat steady.", bestFor: "Coffee drinkers", imgKeyword: "coffee tumbler" },

            // TIME
            { name: "Casio Vintage A158W", price: 1695, tags: ["style", "classic", "safe"], url: "https://www.amazon.in/s?k=Casio+Vintage+A158W", pitch: "A design classic that earns respect from CEOs and Hipsters alike.", bestFor: "Style-conscious", imgKeyword: "casio digital watch" },
            { name: "Canvas Zipper Tote", price: 699, tags: ["carry", "casual", "utility"], url: "https://www.amazon.in/s?k=EcoRight+Canvas+Tote+Bag+Zipper", pitch: "Heavy duty canvas with a zipper. Perfect for lunch + gym gear.", bestFor: "Casual carry", imgKeyword: "canvas tote bag" },
            
            // PREMIUM (Added for "Above 3000" logic)
            { name: "Samsonite Tech Backpack", price: 3800, tags: ["travel", "carry", "safe"], url: "https://www.amazon.in/s?k=Samsonite+Laptop+Backpack", pitch: "The corporate standard. Indestructible build and high status.", bestFor: "Senior Managers", imgKeyword: "black backpack" },
            { name: "Google Nest Mini", price: 3499, tags: ["tech", "setup"], url: "https://www.amazon.in/s?k=Google+Nest+Mini", pitch: "A smart, modern addition to any home office setup.", bestFor: "Tech lovers", imgKeyword: "smart speaker" }
        ];

        // 2. LOGIC
        function getRecommendations(context, budgetMax) {
            let results = [];
            const contextMap = {
                "Desk": ["desk", "setup", "aesthetic", "safe"],
                "Tech": ["tech", "utility", "organized"],
                "Travel": ["travel", "carry", "utility"],
                "Safe": ["safe", "classic", "practical"]
            };
            const targetTags = contextMap[context] || [];

            inventory.forEach(item => {
                // SPECIAL LOGIC: Handle "Above 3000" (budgetMax = 10000)
                if (budgetMax === 10000) {
                    if (item.price < 3000) return; // Skip cheap items
                } else {
                    if (item.price > budgetMax) return; // Standard max filter
                }
                
                let score = 0;
                targetTags.forEach(tag => { if (item.tags.includes(tag)) score += 2; });
                if (item.tags.includes("safe")) score += 1;
                
                if (score > 0 || budgetMax === 10000) results.push({ item, score });
            });

            results.sort((a, b) => b.score - a.score);
            return results.slice(0, 3).map(r => r.item);
        }

        // 3. INTERACTION
        function findGifts() {
            const context = document.getElementById('contextInput').value;
            const budget = parseInt(document.getElementById('budgetInput').value);
            const loading = document.getElementById('loadingState');
            const resultsArea = document.getElementById('resultsArea');
            const cardsContainer = document.getElementById('cardsContainer');
            
            resultsArea.classList.add('hidden');
            loading.classList.remove('hidden');

            confetti({ particleCount: 80, spread: 60, origin: { y: 0.6 }, colors: ['#334155', '#94a3b8'] });

            setTimeout(() => {
                const recs = getRecommendations(context, budget);
                cardsContainer.innerHTML = '';
                
                if (recs.length === 0) {
                    cardsContainer.innerHTML = `
                        <div class="col-span-3 text-center py-12 bg-white rounded-2xl border border-slate-200">
                            <div class="text-4xl mb-3">🤔</div>
                            <h3 class="font-bold text-slate-800 text-lg">Nothing sensible fits this budget yet.</h3>
                            <p class="text-slate-500 mt-2 text-sm">A slightly higher budget opens up better, more reliable options.</p>
                        </div>`;
                } else {
                    recs.forEach(item => {
                        const imgUrl = `https://source.unsplash.com/400x300/?${encodeURIComponent(item.imgKeyword)}`;
                        
                        const cardHTML = `
                            <div class="bg-white rounded-2xl p-5 shadow-sm hover:shadow-xl transition-all border border-slate-100 flex flex-col h-full group transform hover:-translate-y-1 duration-300">
                                <div class="h-48 bg-slate-50 rounded-xl mb-5 overflow-hidden relative">
                                    <img src="${imgUrl}" 
                                         alt="${item.name}" 
                                         class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700"
                                    >
                                    <div class="absolute top-3 right-3 bg-white/95 backdrop-blur px-3 py-1 rounded-lg text-xs font-bold text-slate-700 shadow-sm border border-slate-100">
                                        ₹${item.price}
                                    </div>
                                </div>
                                <p class="text-[10px] font-bold tracking-widest text-slate-400 uppercase mb-2">Safe Professional Choice</p>
                                <h3 class="font-bold text-xl text-slate-900 leading-tight mb-3 brand-font">${item.name}</h3>
                                <div class="flex-grow">
                                    <p class="text-slate-600 text-sm leading-relaxed mb-4">"${item.pitch}"</p>
                                    <div class="flex items-center gap-2 mb-4">
                                        <div class="w-1 h-1 rounded-full bg-slate-300"></div>
                                        <p class="text-xs text-slate-400 italic">Best for: ${item.bestFor}</p>
                                    </div>
                                </div>
                                <a href="${item.url}" target="_blank" class="mt-auto w-full flex items-center justify-center gap-2 border border-slate-200 hover:border-slate-800 hover:bg-slate-800 hover:text-white text-slate-700 font-semibold py-3 rounded-xl transition-all btn-press">
                                    <span>View trusted option</span>
                                    <i data-lucide="arrow-up-right" class="w-4 h-4"></i>
                                </a>
                            </div>`;
                        cardsContainer.innerHTML += cardHTML;
                    });
                    lucide.createIcons();
                }
                loading.classList.add('hidden');
                resultsArea.classList.remove('hidden');
                resultsArea.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 800); 
        }
    </script>
</body>
</html>
"""

# ==========================================
# 3. RENDER THE HTML
# ==========================================
# height=2000 ensures it scrolls naturally like a real site
components.html(html_code, height=2000, scrolling=True)
