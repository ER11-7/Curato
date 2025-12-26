import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Curato | Smart Professional Gifting",
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
    <title>Curato - Professional Gift Scout</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; }
        h1, h2, h3, .brand-font { font-family: 'Poppins', sans-serif; }
        html { scroll-behavior: smooth; }
        @keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .animate-fade-up { animation: fadeUp 0.6s ease-out forwards; }
        .glass-card { background: rgba(255, 255, 255, 0.92); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.6); box-shadow: 0 20px 40px -5px rgba(0, 0, 0, 0.05); }
        .text-gradient { background: linear-gradient(135deg, #0f172a 0%, #334155 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .btn-press:active { transform: scale(0.98); }
        .tab-active { border-bottom: 2px solid #1e293b; color: #1e293b; font-weight: 600; }
        .tab-inactive { color: #94a3b8; }
        @keyframes blob { 0% { transform: translate(0px, 0px) scale(1); } 33% { transform: translate(30px, -50px) scale(1.1); } 66% { transform: translate(-20px, 20px) scale(0.9); } 100% { transform: translate(0px, 0px) scale(1); } }
        .animate-blob { animation: blob 10s infinite; }
        .animation-delay-2000 { animation-delay: 2s; }
        ::-webkit-scrollbar { width: 0px; background: transparent; }
    </style>
</head>
<body class="bg-slate-50 min-h-screen relative overflow-x-hidden selection:bg-slate-200 selection:text-slate-800">

    <!-- Background Decoration -->
    <div class="fixed top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
        <div class="absolute top-[-10%] right-[-5%] w-[600px] h-[600px] bg-blue-50 rounded-full mix-blend-multiply filter blur-3xl opacity-60 animate-blob"></div>
        <div class="absolute top-[20%] left-[-10%] w-[500px] h-[500px] bg-purple-50 rounded-full mix-blend-multiply filter blur-3xl opacity-60 animate-blob animation-delay-2000"></div>
    </div>

    <!-- Navigation -->
    <nav class="w-full px-6 py-6 flex justify-center">
        <div class="glass-card px-8 py-3 rounded-full flex flex-col items-center cursor-pointer hover:shadow-md transition-all duration-300 group">
            <div class="flex items-center gap-2">
                <span class="text-xl group-hover:rotate-12 transition-transform">🎁</span>
                <span class="font-bold text-slate-800 tracking-tight text-lg">Curato</span>
            </div>
            <span class="text-[10px] text-slate-500 font-medium tracking-widest uppercase mt-1">Gifting Intelligence</span>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto px-4 py-10 flex flex-col items-center">
        
        <!-- Hero Section -->
        <div class="text-center mb-8 max-w-2xl animate-fade-up">
            <h1 class="text-4xl md:text-5xl font-extrabold mb-4 leading-tight text-slate-900 brand-font">
                Gift smarter,<br>
                <span class="text-gradient">not harder.</span>
            </h1>
            <p class="text-slate-500 text-lg md:text-xl font-medium leading-relaxed">
                Tell Scout what you need. We'll handle the thinking.
            </p>
        </div>

        <!-- The "App" Card -->
        <div class="w-full glass-card rounded-3xl p-6 md:p-10 mb-12 transform transition-all duration-500 hover:shadow-xl animate-fade-up border-t-4 border-slate-800" style="animation-delay: 0.1s;">
            
            <!-- Tabs -->
            <div class="flex gap-8 mb-8 border-b border-slate-200 pb-2">
                <button onclick="switchTab('quick')" id="tab-quick" class="tab-active pb-2 transition-colors">Quick Filter</button>
                <button onclick="switchTab('chat')" id="tab-chat" class="tab-inactive pb-2 transition-colors hover:text-slate-600 flex items-center gap-2">
                    Ask Scout <span class="bg-indigo-100 text-indigo-600 text-[10px] px-2 py-0.5 rounded-full font-bold">AI</span>
                </button>
            </div>

            <!-- MODE 1: Quick Filter (Dropdowns) -->
            <div id="mode-quick" class="grid grid-cols-1 md:grid-cols-10 gap-8 items-start">
                <div class="md:col-span-5 relative group">
                    <label class="block text-sm font-bold text-slate-800 mb-1 ml-1">Context</label>
                    <div class="relative">
                        <select id="contextInput" class="w-full bg-slate-50 border border-slate-200 text-slate-800 font-medium text-base py-4 px-4 rounded-xl appearance-none focus:outline-none focus:border-slate-800 focus:bg-white transition-colors cursor-pointer shadow-sm">
                            <option value="Desk">Desk Essentials</option>
                            <option value="Tech">Tech & Gadgets</option>
                            <option value="Travel">Travel & Commute</option>
                            <option value="Safe">Safe & Neutral</option>
                        </select>
                        <div class="absolute top-4 right-4 flex items-center pointer-events-none text-slate-400"><i data-lucide="chevron-down"></i></div>
                    </div>
                </div>
                <div class="md:col-span-3 relative group">
                    <label class="block text-sm font-bold text-slate-800 mb-1 ml-1">Budget</label>
                    <div class="relative">
                        <select id="budgetInput" class="w-full bg-slate-50 border border-slate-200 text-slate-800 font-medium text-base py-4 px-4 rounded-xl appearance-none focus:outline-none focus:border-slate-800 focus:bg-white transition-colors cursor-pointer shadow-sm">
                            <option value="500">Under ₹500</option>
                            <option value="1500" selected>₹500 – ₹1,500</option>
                            <option value="3000">₹1,500 – ₹3,000</option>
                            <option value="10000">Above ₹3,000</option>
                        </select>
                        <div class="absolute top-4 right-4 flex items-center pointer-events-none text-slate-400"><i data-lucide="chevron-down"></i></div>
                    </div>
                </div>
                <div class="md:col-span-2 flex flex-col justify-end h-full">
                    <button onclick="findGifts('filter')" class="btn-press w-full bg-slate-800 hover:bg-slate-900 text-white font-semibold text-base py-4 px-6 rounded-xl shadow-lg shadow-slate-200 transition-all flex items-center justify-center gap-2 group">
                        <span>Find</span>
                        <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </button>
                </div>
            </div>

            <!-- MODE 2: Ask Scout (Text Input) -->
            <div id="mode-chat" class="hidden">
                <label class="block text-sm font-bold text-slate-800 mb-2 ml-1">Describe who it's for...</label>
                <div class="relative flex items-center">
                    <input type="text" id="chatInput" placeholder="e.g. 'A manager who loves coffee and travels a lot'" 
                           class="w-full bg-slate-50 border border-slate-200 text-slate-800 font-medium text-base py-4 px-4 pr-16 rounded-xl focus:outline-none focus:border-slate-800 focus:bg-white transition-colors shadow-sm"
                           onkeypress="handleKeyPress(event)">
                    <button onclick="findGifts('chat')" class="absolute right-2 bg-slate-800 hover:bg-slate-900 text-white p-2.5 rounded-lg transition-colors">
                        <i data-lucide="sparkles" class="w-5 h-5"></i>
                    </button>
                </div>
                <p class="text-xs text-slate-400 mt-2 ml-1">Try keywords like "coffee", "travel", "music", "writing", "tech".</p>
            </div>

        </div>

        <!-- Loading State -->
        <div id="loadingState" class="hidden py-12 text-center animate-fade-up">
            <div class="relative w-16 h-16 mx-auto mb-4">
                <div class="absolute top-0 left-0 w-full h-full border-4 border-slate-100 rounded-full"></div>
                <div class="absolute top-0 left-0 w-full h-full border-4 border-slate-800 rounded-full border-t-transparent animate-spin"></div>
            </div>
            <h3 class="text-slate-800 font-semibold text-lg">Scout is looking...</h3>
        </div>

        <!-- Results Grid -->
        <div id="resultsArea" class="hidden w-full animate-fade-up">
            <div class="flex justify-between items-end mb-6 border-b border-slate-200 pb-4">
                <div>
                    <h2 class="text-2xl font-bold text-slate-900 brand-font">Shortlisted for you</h2>
                    <p class="text-slate-500 text-sm mt-1">Safe, professional choices.</p>
                </div>
                <button onclick="shuffleResults()" class="text-sm font-semibold text-slate-600 hover:text-slate-900 flex items-center gap-1 transition-colors">
                    <i data-lucide="refresh-cw" class="w-4 h-4"></i> Show different options
                </button>
            </div>
            
            <div id="cardsContainer" class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Cards injected via JS -->
            </div>
        </div>

    </main>

    <footer class="mt-12 py-8 text-center text-slate-400 text-sm border-t border-slate-100 bg-white">
        <p>&copy; 2025 Curato. Built for Indian workplaces.</p>
    </footer>

    <!-- Logic Script -->
    <script>
        lucide.createIcons();

        // 1. EXPANDED INVENTORY WITH FIXED IMAGE IDs (No more broken images)
        const inventory = [
            // DESK & WRITING
            { name: "Parker Vector Pen", price: 450, tags: ["safe", "desk", "classic", "writing"], url: "https://www.amazon.in/s?k=Parker+Vector+Stainless+Steel+CT+Ball+Pen", pitch: "The universal symbol of a professional gift.", bestFor: "Formal settings", imgId: "1585336261022-680e295ce3fe" },
            { name: "Factor Notes Journal", price: 499, tags: ["desk", "creative", "safe", "writing"], url: "https://www.amazon.in/s?k=Factor+Notes+Hardcover+Notebook+A5", pitch: "Premium paper for serious thinkers.", bestFor: "Planners", imgId: "1544816155-12df9643f363" },
            { name: "Moleskine Classic", price: 1900, tags: ["desk", "creative", "premium", "writing"], url: "https://www.amazon.in/s?k=Moleskine+Classic+Notebook", pitch: "The legendary notebook used by artists and thinkers.", bestFor: "Creatives", imgId: "1517842645728-3a6f23dcd405" },
            { name: "Lamy Safari Pen", price: 2400, tags: ["desk", "creative", "premium", "writing"], url: "https://www.amazon.in/s?k=Lamy+Safari+Fountain+Pen", pitch: "German engineering in a pen. Cult classic.", bestFor: "Designers", imgId: "1583485056328-1f788cbb35bc" },
            { name: "Vegan Leather Desk Mat", price: 799, tags: ["desk", "setup", "aesthetic"], url: "https://www.amazon.in/s?k=Vegan+Leather+Desk+Mat+Extended", pitch: "Instantly makes a desk look executive.", bestFor: "New setups", imgId: "1616628188823-14b354316d37" },
            { name: "Bamboo Desk Organizer", price: 850, tags: ["desk", "organized", "eco"], url: "https://www.amazon.in/s?k=Bamboo+Desk+Organizer", pitch: "Sustainable and stylish organization.", bestFor: "Eco-conscious", imgId: "1506084868230-bb9d95c24759" },

            // TECH & GADGETS
            { name: "Alloy Laptop Stand", price: 699, tags: ["tech", "health", "desk"], url: "https://www.amazon.in/s?k=Portronics+My+Buddy+K+Portable+Laptop+Stand", pitch: "Saves their neck. Folds into a stick.", bestFor: "Laptop users", imgId: "1611186871348-b1ce696e52c9" },
            { name: "DailyObjects Tech Kit", price: 1299, tags: ["tech", "travel", "organized"], url: "https://www.amazon.in/s?k=DailyObjects+Tech+Kit+Organizer", pitch: "Fixes the cable mess. Essential for hybrid work.", bestFor: "Hybrid workers", imgId: "1553062407-98eeb64c6a62" },
            { name: "SanDisk Dual Drive", price: 899, tags: ["tech", "utility", "budget"], url: "https://www.amazon.in/s?k=SanDisk+Ultra+Dual+Drive+Go+Type-C", pitch: "High utility choice. Transfers data between phone & laptop instantly.", bestFor: "Tech roles", imgId: "1623945415372-2d113f363c32" },
            { name: "Logitech Pebble Mouse", price: 1400, tags: ["tech", "aesthetic", "productivity"], url: "https://www.amazon.in/s?k=Logitech+Pebble+Mouse", pitch: "Minimalist, silent, and beautiful.", bestFor: "Designers", imgId: "1527864550417-7fd91fc51a46" },
            { name: "Portronics SoundDrum", price: 1800, tags: ["tech", "music", "fun"], url: "https://www.amazon.in/s?k=Portronics+SoundDrum", pitch: "Great sound in a small package.", bestFor: "Music lovers", imgId: "1608043152269-423dbba4e7e1" },
            { name: "Anker PowerCore", price: 2200, tags: ["tech", "travel", "utility"], url: "https://www.amazon.in/s?k=Anker+PowerCore+10000", pitch: "The most reliable power bank.", bestFor: "Travelers", imgId: "1609091839311-d5365f9ff1c5" },
            { name: "Cable Organiser Clips", price: 399, tags: ["tech", "budget", "organized"], url: "https://www.amazon.in/s?k=Cable+Clips+Organizer", pitch: "Simple utility for messy desks.", bestFor: "Everyone", imgId: "1586776977607-310e9c725c37" },

            // COFFEE & FOOD
            { name: "Milton Thermosteel", price: 750, tags: ["utility", "travel", "safe", "coffee"], url: "https://www.amazon.in/s?k=Milton+Thermosteel+Flip+Lid+500ml", pitch: "Keeps coffee hot for 4 hours.", bestFor: "Daily hydration", imgId: "1602143407151-011141950038" },
            { name: "Borosil Glass Lunch Set", price: 950, tags: ["health", "food", "practical"], url: "https://www.amazon.in/s?k=Borosil+Glass+Lunch+Box+Set+of+3", pitch: "Premium glass, microwave safe.", bestFor: "Office lunches", imgId: "1587393855524-087f83d95bc9" },
            { name: "Vaya Drynk Tumbler", price: 1600, tags: ["coffee", "premium", "travel"], url: "https://www.amazon.in/s?k=Vaya+Drynk", pitch: "The most stylish tumbler on the market.", bestFor: "Coffee snobs", imgId: "1514228742587-6b1558fcca3d" },
            { name: "French Press", price: 1200, tags: ["coffee", "home", "aesthetic"], url: "https://www.amazon.in/s?k=Instacuppa+French+Press", pitch: "For serious coffee lovers.", bestFor: "Coffee lovers", imgId: "1556742502-ec7844db6e88" },
            { name: "Electric Lunch Box", price: 1100, tags: ["food", "tech", "utility"], url: "https://www.amazon.in/s?k=Milton+Electric+Lunch+Box", pitch: "Hot food at your desk, no microwave needed.", bestFor: "Desk diners", imgId: "1627308595229-7830a5c91f9f" },

            // TRAVEL & CARRY
            { name: "Sleek Laptop Sleeve", price: 999, tags: ["carry", "minimalist", "safe"], url: "https://www.amazon.in/s?k=Vegan+Leather+Laptop+Sleeve+15.6", pitch: "Slim protection.", bestFor: "Commuters", imgId: "1560769629-975ec94e6a86" },
            { name: "EcoRight Canvas Tote", price: 699, tags: ["carry", "casual", "utility", "eco"], url: "https://www.amazon.in/s?k=EcoRight+Canvas+Tote+Bag+Zipper", pitch: "Heavy duty canvas with zipper.", bestFor: "Casual carry", imgId: "1597484662317-c93125131818" },
            { name: "Passport Holder", price: 800, tags: ["travel", "safe", "leather"], url: "https://www.amazon.in/s?k=Premium+Passport+Holder", pitch: "For the frequent flyer.", bestFor: "Travelers", imgId: "1544816155-12df9643f363" },
            
            // PREMIUM
            { name: "Samsonite Tech Backpack", price: 3800, tags: ["travel", "carry", "safe", "premium"], url: "https://www.amazon.in/s?k=Samsonite+Laptop+Backpack", pitch: "Corporate standard. Indestructible.", bestFor: "Senior Managers", imgId: "1553062407-98eeb64c6a62" },
            { name: "Google Nest Mini", price: 3499, tags: ["tech", "setup", "home"], url: "https://www.amazon.in/s?k=Google+Nest+Mini", pitch: "Smart assistant for the home office.", bestFor: "Tech lovers", imgId: "1543512214-318c77a9e254" }
        ];

        let currentResults = [];
        let startIndex = 0;

        // 2. TABS LOGIC
        function switchTab(mode) {
            document.getElementById('mode-quick').classList.add('hidden');
            document.getElementById('mode-chat').classList.add('hidden');
            document.getElementById('tab-quick').className = "tab-inactive pb-2 transition-colors hover:text-slate-600";
            document.getElementById('tab-chat').className = "tab-inactive pb-2 transition-colors hover:text-slate-600 flex items-center gap-2";
            
            document.getElementById('mode-' + mode).classList.remove('hidden');
            document.getElementById('tab-' + mode).className = "tab-active pb-2 transition-colors";
        }

        // 3. RECOMMENDATION ENGINE (Hybrid)
        function getRecommendations(mode) {
            let results = [];
            let budgetMax = 100000;
            let filterTags = [];

            if (mode === 'filter') {
                const context = document.getElementById('contextInput').value;
                const budgetVal = parseInt(document.getElementById('budgetInput').value);
                budgetMax = budgetVal === 10000 ? 100000 : budgetVal;
                
                const contextMap = {
                    "Desk": ["desk", "setup", "writing", "organized"],
                    "Tech": ["tech", "utility", "organized", "music"],
                    "Travel": ["travel", "carry", "utility", "coffee"],
                    "Safe": ["safe", "classic", "practical", "home"]
                };
                filterTags = contextMap[context] || [];
            } 
            else if (mode === 'chat') {
                const text = document.getElementById('chatInput').value.toLowerCase();
                if (text.includes("coffee") || text.includes("tea")) filterTags.push("coffee");
                if (text.includes("travel") || text.includes("fly") || text.includes("commute")) filterTags.push("travel", "carry");
                if (text.includes("tech") || text.includes("gadget")) filterTags.push("tech");
                if (text.includes("write") || text.includes("note")) filterTags.push("writing");
                if (text.includes("manager") || text.includes("boss")) filterTags.push("premium", "classic");
                if (text.includes("music") || text.includes("audio")) filterTags.push("music");
                if (text.includes("eco") || text.includes("green")) filterTags.push("eco");
                if (filterTags.length === 0) filterTags.push("safe");
            }

            // Scoring
            inventory.forEach(item => {
                // Budget Logic
                if (mode === 'filter') {
                    const budgetVal = parseInt(document.getElementById('budgetInput').value);
                    if (budgetVal === 10000) {
                        if (item.price < 3000) return; // Only show premium items
                    } else {
                        if (item.price > budgetMax) return; // Standard max cap
                    }
                }

                let score = 0;
                filterTags.forEach(tag => { if (item.tags.includes(tag)) score += 3; });
                if (item.tags.includes("safe")) score += 1;
                
                if (score > 0) results.push({ item, score });
            });

            // Shuffle results with same score for variety
            results.sort((a, b) => b.score - a.score || 0.5 - Math.random());
            return results.map(r => r.item);
        }

        // 4. UI RENDERER
        function findGifts(mode) {
            const loading = document.getElementById('loadingState');
            const resultsArea = document.getElementById('resultsArea');
            
            resultsArea.classList.add('hidden');
            loading.classList.remove('hidden');
            confetti({ particleCount: 50, spread: 60, origin: { y: 0.6 }, colors: ['#334155', '#94a3b8'] });

            setTimeout(() => {
                currentResults = getRecommendations(mode);
                startIndex = 0;
                renderCards();
                loading.classList.add('hidden');
                resultsArea.classList.remove('hidden');
                resultsArea.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 600);
        }

        function renderCards() {
            const cardsContainer = document.getElementById('cardsContainer');
            cardsContainer.innerHTML = '';
            
            const batch = currentResults.slice(startIndex, startIndex + 3);
            
            if (batch.length === 0) {
                if (startIndex === 0) {
                    cardsContainer.innerHTML = `<div class="col-span-3 text-center py-10"><h3 class="font-bold text-slate-700">No specific matches.</h3><p class="text-slate-500">Try broad keywords like "Office" or "Travel".</p></div>`;
                } else {
                    startIndex = 0;
                    renderCards(); 
                    return;
                }
            } else {
                batch.forEach(item => {
                    const imgUrl = `https://images.unsplash.com/photo-${item.imgId}?auto=format&fit=crop&w=400&q=80`;
                    
                    cardsContainer.innerHTML += `
                        <div class="bg-white rounded-2xl p-5 shadow-sm hover:shadow-xl transition-all border border-slate-100 flex flex-col h-full group transform hover:-translate-y-1 duration-300 animate-fade-up">
                            <div class="h-48 bg-slate-50 rounded-xl mb-5 overflow-hidden relative">
                                <img src="${imgUrl}" 
                                     class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                                     loading="lazy"
                                     onerror="this.src='https://placehold.co/400x300?text=${encodeURIComponent(item.name)}'">
                                <div class="absolute top-3 right-3 bg-white/95 backdrop-blur px-3 py-1 rounded-lg text-xs font-bold text-slate-700 shadow-sm border border-slate-100">₹${item.price}</div>
                            </div>
                            <p class="text-[10px] font-bold tracking-widest text-slate-400 uppercase mb-2">Safe Choice</p>
                            <h3 class="font-bold text-xl text-slate-900 leading-tight mb-3 brand-font">${item.name}</h3>
                            <div class="flex-grow">
                                <p class="text-slate-600 text-sm leading-relaxed mb-4">"${item.pitch}"</p>
                                <div class="flex items-center gap-2 mb-4"><div class="w-1 h-1 rounded-full bg-slate-300"></div><p class="text-xs text-slate-400 italic">Best for: ${item.bestFor}</p></div>
                            </div>
                            <a href="${item.url}" target="_blank" class="mt-auto w-full flex items-center justify-center gap-2 border border-slate-200 hover:border-slate-800 hover:bg-slate-800 hover:text-white text-slate-700 font-semibold py-3 rounded-xl transition-all btn-press">
                                <span>View trusted option</span><i data-lucide="arrow-up-right" class="w-4 h-4"></i>
                            </a>
                        </div>`;
                });
            }
            lucide.createIcons();
        }

        function shuffleResults() {
            startIndex += 3;
            if (startIndex >= currentResults.length) startIndex = 0;
            renderCards();
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter') findGifts('chat');
        }
    </script>
</body>
</html>
"""

# ==========================================
# 3. RENDER THE HTML
# ==========================================
components.html(html_code, height=2000, scrolling=True)
