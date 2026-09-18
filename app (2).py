import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="المحاضرة 1 | مقدمة في الذكاء الاصطناعي",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# GLOBAL STYLE
# =========================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;600;700;800&display=swap');

    :root {
        --navy: #12395B;
        --navy-2: #1B4F72;
        --teal: #2A9D8F;
        --teal-dark: #18786F;
        --sky: #EAF4FB;
        --mint: #EAF8F5;
        --ink: #203040;
        --muted: #68798A;
        --line: #DCE7EF;
        --white: #FFFFFF;
        --warm: #F7FAFC;
        --accent: #E9C46A;
        --danger-soft: #FFF4EE;
        --danger: #C96D45;
        --success-soft: #EEF9F5;
    }

    html, body, [class*="css"], .stApp {
        font-family: "Tajawal", "Arial", sans-serif !important;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 0%, rgba(42,157,143,.08), transparent 26%),
            radial-gradient(circle at 100% 10%, rgba(18,57,91,.06), transparent 23%),
            #F8FBFD;
        color: var(--ink);
    }

    /* RTL across main content */
    .main .block-container,
    section.main,
    div[data-testid="stMarkdownContainer"] {
        direction: rtl;
        text-align: right;
    }

    .main .block-container {
        max-width: 1180px;
        padding-top: 1.35rem;
        padding-bottom: 3rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        direction: rtl;
        background: linear-gradient(180deg, #12395B 0%, #0F2F4B 100%);
        border-left: 1px solid rgba(255,255,255,.08);
    }
    section[data-testid="stSidebar"] * {
        font-family: "Tajawal", "Arial", sans-serif !important;
    }
    section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] {
        color: white;
    }
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span {
        color: #F7FBFF !important;
    }
    section[data-testid="stSidebar"] [data-testid="stRadio"] > div {
        gap: .20rem;
    }

    /* Hide default Streamlit chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header[data-testid="stHeader"] {background: transparent;}

    /* Typography */
    h1, h2, h3, h4 {
        font-family: "Tajawal", "Arial", sans-serif !important;
        color: var(--navy);
        letter-spacing: 0;
    }
    h1 {font-weight: 800 !important;}
    h2 {font-weight: 800 !important;}
    h3 {font-weight: 700 !important;}

    /* Hero */
    .hero {
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, #12395B 0%, #1B557D 56%, #2A9D8F 130%);
        border-radius: 28px;
        padding: 34px 38px 30px;
        color: white;
        box-shadow: 0 16px 42px rgba(18, 57, 91, .18);
        margin-bottom: 24px;
    }
    .hero:after {
        content: "";
        position: absolute;
        width: 260px;
        height: 260px;
        border-radius: 50%;
        background: rgba(255,255,255,.08);
        left: -85px;
        top: -90px;
    }
    .hero:before {
        content: "";
        position: absolute;
        width: 170px;
        height: 170px;
        border-radius: 50%;
        border: 1px solid rgba(255,255,255,.15);
        right: -35px;
        bottom: -70px;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,.13);
        border: 1px solid rgba(255,255,255,.18);
        border-radius: 999px;
        padding: 7px 13px;
        font-size: .92rem;
        font-weight: 700;
        margin-bottom: 13px;
    }
    .hero h1 {
        color: white !important;
        font-size: 2.25rem !important;
        line-height: 1.35 !important;
        margin: 0 0 8px !important;
    }
    .hero p {
        color: #EAF5FA !important;
        font-size: 1.08rem;
        line-height: 1.9;
        margin: 0;
        max-width: 860px;
    }
    .hero-meta {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 22px;
    }
    .hero-chip {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 8px 12px;
        background: rgba(255,255,255,.10);
        border: 1px solid rgba(255,255,255,.15);
        border-radius: 12px;
        font-size: .9rem;
        color: white;
    }

    /* Section heading */
    .section-kicker {
        color: var(--teal-dark);
        font-size: .82rem;
        font-weight: 800;
        letter-spacing: .3px;
        margin-bottom: 4px;
    }
    .section-title {
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 0 0 8px;
    }
    .section-title .num {
        width: 38px;
        height: 38px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex: 0 0 38px;
        border-radius: 12px;
        color: white;
        background: var(--navy);
        font-weight: 800;
        font-size: .95rem;
        box-shadow: 0 7px 18px rgba(18,57,91,.15);
    }
    .section-title h2 {
        margin: 0 !important;
        font-size: 1.65rem !important;
    }
    .lead {
        color: var(--muted);
        font-size: 1rem;
        line-height: 1.9;
        margin-bottom: 18px;
    }

    /* Cards */
    .card {
        background: var(--white);
        border: 1px solid var(--line);
        border-radius: 19px;
        padding: 20px 21px;
        box-shadow: 0 8px 25px rgba(32,48,64,.055);
        height: 100%;
    }
    .card h3 {
        font-size: 1.08rem !important;
        margin: 0 0 8px !important;
        color: var(--navy) !important;
    }
    .card p {
        margin: 0;
        color: var(--muted);
        line-height: 1.8;
    }

    .mini-card {
        background: white;
        border: 1px solid var(--line);
        border-top: 4px solid var(--teal);
        border-radius: 17px;
        padding: 18px;
        min-height: 142px;
        box-shadow: 0 6px 18px rgba(32,48,64,.045);
    }
    .mini-card .en {
        color: var(--teal-dark);
        font-size: .79rem;
        font-weight: 800;
        margin-bottom: 3px;
    }
    .mini-card .ar {
        color: var(--navy);
        font-size: 1.08rem;
        font-weight: 800;
        margin-bottom: 7px;
    }
    .mini-card .desc {
        color: var(--muted);
        font-size: .92rem;
        line-height: 1.7;
    }

    /* Callouts */
    .callout {
        border-radius: 18px;
        padding: 17px 19px;
        margin: 13px 0;
        border: 1px solid;
        line-height: 1.9;
    }
    .callout strong {color: var(--navy);}
    .callout.info {
        background: #EEF6FB;
        border-color: #D2E7F3;
    }
    .callout.success {
        background: var(--success-soft);
        border-color: #CFEDE4;
    }
    .callout.warn {
        background: #FFF8E8;
        border-color: #F5E3AE;
    }
    .callout.danger {
        background: var(--danger-soft);
        border-color: #F2D5C8;
    }

    /* Pill */
    .pill {
        display: inline-block;
        border-radius: 999px;
        padding: 5px 10px;
        margin: 3px;
        background: var(--sky);
        color: var(--navy);
        font-size: .86rem;
        font-weight: 700;
        border: 1px solid #D5E7F3;
    }

    /* Compare */
    .compare-title {
        font-size: .92rem;
        font-weight: 800;
        color: var(--navy);
        margin-bottom: 8px;
    }
    .compare-box {
        background: white;
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 19px;
        min-height: 235px;
        box-shadow: 0 7px 22px rgba(32,48,64,.05);
    }
    .compare-box.traditional {border-top: 5px solid #8FA7B8;}
    .compare-box.ai {border-top: 5px solid var(--teal);}
    .compare-box ul {
        margin: 8px 0 0;
        padding-right: 18px;
        color: var(--muted);
        line-height: 2;
    }

    /* Flow */
    .flow {
        display: flex;
        align-items: stretch;
        gap: 10px;
        flex-wrap: wrap;
        margin: 16px 0;
    }
    .flow-step {
        flex: 1 1 145px;
        background: white;
        border: 1px solid var(--line);
        border-radius: 16px;
        padding: 15px 13px;
        text-align: center;
        box-shadow: 0 6px 17px rgba(32,48,64,.04);
    }
    .flow-step .n {
        width: 28px;
        height: 28px;
        margin: 0 auto 9px;
        border-radius: 9px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: var(--navy);
        color: white;
        font-size: .82rem;
        font-weight: 800;
    }
    .flow-step b {color: var(--navy);}
    .flow-step small {
        display: block;
        color: var(--muted);
        margin-top: 5px;
        line-height: 1.55;
    }

    /* Table */
    .table-wrap {
        overflow-x: auto;
        border-radius: 18px;
        border: 1px solid var(--line);
        background: white;
        box-shadow: 0 7px 22px rgba(32,48,64,.045);
        margin: 15px 0;
    }
    table.clean {
        width: 100%;
        border-collapse: collapse;
        min-width: 760px;
        direction: rtl;
    }
    table.clean thead th {
        background: var(--navy);
        color: white;
        padding: 14px 15px;
        font-size: .95rem;
        font-weight: 800;
        text-align: right;
    }
    table.clean tbody td {
        padding: 13px 15px;
        border-bottom: 1px solid #E7EEF3;
        color: #33485A;
        line-height: 1.65;
        background: white;
    }
    table.clean tbody tr:nth-child(even) td {
        background: #FBFDFE;
    }
    table.clean tbody tr:last-child td {
        border-bottom: 0;
    }

    /* Hierarchy */
    .hierarchy {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        gap: 10px;
        margin: 20px auto;
        max-width: 820px;
    }
    .layer {
        border-radius: 18px;
        text-align: center;
        padding: 18px 24px;
        color: white;
        font-weight: 800;
        box-shadow: 0 7px 20px rgba(18,57,91,.10);
    }
    .layer.ai-layer {width: 90%; background: #12395B;}
    .layer.ml-layer {width: 68%; background: #1B6A83;}
    .layer.dl-layer {width: 46%; background: #2A9D8F;}
    .layer span {
        display: block;
        font-size: .82rem;
        font-weight: 500;
        opacity: .88;
        margin-top: 3px;
    }

    /* Timeline */
    .timeline-item {
        position: relative;
        background: white;
        border: 1px solid var(--line);
        border-right: 5px solid var(--teal);
        border-radius: 15px;
        padding: 14px 16px;
        margin-bottom: 10px;
    }
    .timeline-item b {color: var(--navy);}
    .timeline-item p {margin: 4px 0 0; color: var(--muted);}

    /* Quiz */
    div[data-testid="stForm"] {
        background: white;
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 18px 18px 8px;
        box-shadow: 0 8px 26px rgba(32,48,64,.05);
    }
    .stButton > button, .stFormSubmitButton > button {
        border: none !important;
        border-radius: 12px !important;
        background: var(--navy) !important;
        color: white !important;
        font-weight: 800 !important;
        padding: .65rem 1.2rem !important;
    }
    .stButton > button:hover, .stFormSubmitButton > button:hover {
        background: var(--navy-2) !important;
    }

    /* Small citation / footer */
    .source-note {
        color: #7C8C99;
        font-size: .80rem;
        line-height: 1.7;
        margin-top: 7px;
    }

    /* Responsive */
    @media (max-width: 760px) {
        .hero {padding: 25px 22px;}
        .hero h1 {font-size: 1.75rem !important;}
        .main .block-container {padding-left: .8rem; padding-right: .8rem;}
        .section-title h2 {font-size: 1.38rem !important;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HELPERS
# =========================================================
def section_header(num, title, intro=None, kicker="المحاضرة الثانية"):
    st.markdown(
        f"""
        <div class="section-kicker">{kicker}</div>
        <div class="section-title">
            <span class="num">{num}</span>
            <h2>{title}</h2>
        </div>
        {f'<div class="lead">{intro}</div>' if intro else ''}
        """,
        unsafe_allow_html=True,
    )

def callout(text, kind="info"):
    st.markdown(f'<div class="callout {kind}">{text}</div>', unsafe_allow_html=True)

def mini_card(en, ar, desc):
    st.markdown(
        f"""
        <div class="mini-card">
            <div class="en">{en}</div>
            <div class="ar">{ar}</div>
            <div class="desc">{desc}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def clean_table(headers, rows):
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = ""
    for row in rows:
        body += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
    st.markdown(
        f"""
        <div class="table-wrap">
            <table class="clean">
                <thead><tr>{head}</tr></thead>
                <tbody>{body}</tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================

# SIDEBAR
# =========================================================
sections = [
    "الرئيسية",
    "1. لماذا ندرس تاريخ AI؟",
    "2. Turing - 1950",
    "3. Dartmouth - 1956",
    "4. Symbolic AI",
    "5. التفاؤل المبكر والحدود",
    "6. AI Winter",
    "7. Expert Systems",
    "8. Machine Learning",
    "9. Deep Learning",
    "10. محطات التطور الحديث",
    "11. Transformer - 2017",
    "12. Large Language Models",
    "13. RLHF واتباع التعليمات",
    "14. Generative AI",
    "15. AI في المؤسسة عبر الزمن",
    "16. TD وQuiz",
    "17. الخلاصة والمراجع",
]

with st.sidebar:
    st.markdown("## تاريخ الذكاء الاصطناعي وتطوره")
    st.markdown("**السنة الثانية ليسانس – علوم التسيير**")
    st.markdown("---")
    selected = st.radio("خريطة المحاضرة", sections, label_visibility="collapsed")
    idx = sections.index(selected)
    st.progress(idx / (len(sections)-1))
    st.caption(f"التقدم داخل المحاضرة: {idx}/{len(sections)-1}")
    st.markdown("---")
    st.markdown(
        """<div style="font-size:.85rem; line-height:1.8; color:#DCEBF4;">
        هذه المحاضرة تركز على منطق التطور التاريخي، لا على حفظ التواريخ فقط.
        </div>""",
        unsafe_allow_html=True,
    )

# HERO
# =========================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">المحاضرة 02</div>
        <h1>تاريخ الذكاء الاصطناعي وتطوره</h1>
        <p>
        من سؤال Alan Turing في 1950 إلى Symbolic AI وExpert Systems، ثم
        Machine Learning وDeep Learning وTransformer وصولًا إلى
        Large Language Models وGenerative AI.
        </p>
        <div class="hero-meta">
            <span class="hero-chip">History of AI</span>
            <span class="hero-chip">السنة الثانية – علوم التسيير</span>
            <span class="hero-chip">فهم التطور لا حفظ التواريخ فقط</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if selected == "الرئيسية":
    section_header("00", "أهداف المحاضرة",
                   "نفهم المراحل الأساسية، وأسباب الانتقال من القواعد إلى التعلم من البيانات ثم إلى النماذج التوليدية.")
    cols = st.columns(3)
    items = [
        ("Identify", "تحديد المراحل", "التعرف على المحطات التاريخية الكبرى من 1950 إلى عصر Generative AI."),
        ("Explain", "تفسير التحولات", "تفسير لماذا انتقل المجال من Rules إلى Learning from Data."),
        ("Distinguish", "التمييز", "الفرق بين Symbolic AI وMachine Learning وDeep Learning وGenerative AI."),
        ("Understand", "فهم AI Winter", "لماذا تراجع التمويل والحماس في فترات معينة؟"),
        ("Connect", "الربط بالإدارة", "كيف تغيرت قيمة AI للمؤسسة مع تطور التقنية؟"),
        ("Review", "المراجعة", "خط زمني، مقارنات، TD وQuiz تفاعلي."),
    ]
    for i, item in enumerate(items):
        with cols[i % 3]:
            mini_card(*item)
    callout("<strong>الخيط العام:</strong> Rules → Data → Learning → Deep Learning → Transformer → LLMs → Generative AI.", "success")

elif selected == "1. لماذا ندرس تاريخ AI؟":
    section_header("01", "لماذا ندرس تاريخ الذكاء الاصطناعي؟",
                   "التاريخ يساعدنا على فهم قدرات الأنظمة الحالية وحدودها.")
    c1, c2 = st.columns(2)
    with c1:
        mini_card("Origins", "أصل الأفكار", "كثير من الأفكار الأساسية قديمة، لكن تطبيقها احتاج بيانات وحوسبة أفضل.")
        mini_card("Methods", "تغير المناهج", "من كتابة القواعد يدويًا إلى التعلم من البيانات.")
    with c2:
        mini_card("Cycles", "دورات التوقعات", "مر AI بفترات تفاؤل قوي ثم تراجع في التمويل والاهتمام.")
        mini_card("Business", "القيمة المؤسسية", "من أنظمة متخصصة إلى أدوات عامة للعمل المعرفي والقرار.")
    callout("<strong>قاعدة:</strong> التاريخ ليس قائمة تواريخ. ابحث دائمًا عن: المشكلة → الحل → الحدود → المنهج الجديد.", "info")

elif selected == "2. Turing - 1950":
    section_header("02", "Alan Turing – 1950", "Computing Machinery and Intelligence")
    callout("<strong>السؤال الشهير:</strong> Can machines think? – هل تستطيع الآلات التفكير؟", "success")
    st.markdown("في 1950 نشر Alan Turing مقاله الشهير في مجلة *Mind*. وبدل محاولة تعريف «التفكير» فلسفيًا فقط، اقترح **Imitation Game** الذي أصبح معروفًا باسم **Turing Test**.")
    clean_table(["العنصر", "التفسير"], [
        ["المشارك", "يتواصل نصيًا مع طرفين دون رؤيتهما."],
        ["الطرفان", "أحدهما إنسان والآخر آلة."],
        ["المهمة", "محاولة التمييز بين الإنسان والآلة."],
        ["المغزى", "اختبار سلوكي لقدرة الآلة على تقديم تفاعل مقنع."],
    ])
    callout("Turing Test لا يثبت أن الآلة تفكر بالطريقة نفسها التي يفكر بها الإنسان؛ هو يركز على السلوك الظاهر في التفاعل.", "warn")

elif selected == "3. Dartmouth - 1956":
    section_header("03", "Dartmouth – 1956", "ولادة Artificial Intelligence كحقل بحثي")
    st.markdown("في 1955 أعد John McCarthy وMarvin Minsky وNathaniel Rochester وClaude Shannon مقترحًا لمشروع صيفي عقد في Dartmouth College في 1956.")
    cols = st.columns(2)
    for i, item in enumerate([
        ("Language", "استخدام اللغة", "كيف نجعل الآلة تتعامل مع اللغة؟"),
        ("Concepts", "المفاهيم", "كيف تكوّن الآلة التجريدات والمفاهيم؟"),
        ("Problem Solving", "حل المشكلات", "كيف تنجز مهامًا كانت تُعد حكرًا على الإنسان؟"),
        ("Self-improvement", "التحسين", "كيف يمكن للنظام تحسين أدائه؟"),
    ]):
        with cols[i % 2]:
            mini_card(*item)
    callout("<strong>لا تخلط:</strong> 1950 = سؤال Turing. 1956 = ترسيخ AI كاسم لمجال بحثي.", "success")

elif selected == "4. Symbolic AI":
    section_header("04", "Symbolic AI", "Rules, symbols and logic")
    st.markdown("في المراحل المبكرة ركز الباحثون على تمثيل المعرفة في صورة رموز وقواعد منطقية يمكن للحاسوب تطبيقها.")
    clean_table(["القاعدة", "النتيجة"], [
        ["IF العميل لم يدفع الفاتورة AND تجاوز تاريخ الاستحقاق", "THEN أرسل تنبيهًا"],
        ["IF المديونية مرتفعة AND السيولة منخفضة", "THEN ارفع مستوى المخاطر"],
    ])
    c1, c2 = st.columns(2)
    with c1:
        mini_card("Strength", "الميزة", "القواعد واضحة ويمكن تتبع سبب الاستنتاج.")
    with c2:
        mini_card("Limit", "الحد", "من الصعب كتابة كل قواعد الواقع والتعامل مع الاستثناءات.")
    callout("<strong>الفكرة:</strong> في Symbolic AI يكتب الإنسان المعرفة، والنظام يطبقها.", "info")

elif selected == "5. التفاؤل المبكر والحدود":
    section_header("05", "التفاؤل المبكر وحدود الحوسبة",
                   "نجاحات مبكرة، لكن المشكلات الواقعية كانت أكثر تعقيدًا.")
    clean_table(["بيئة التجربة", "الواقع"], [
        ["مشكلات محددة وقواعد واضحة", "معلومات ناقصة ومتغيرة"],
        ["عدد حالات محدود", "عدد هائل من الاحتمالات"],
        ["بيانات منظمة", "بيانات غير منظمة ومعقدة"],
        ["بيئة يمكن التحكم فيها", "أسواق ومؤسسات متغيرة"],
    ])
    callout("الفجوة بين التوقعات والقدرات الفعلية ساهمت في فترات تراجع الحماس والتمويل.", "warn")

elif selected == "6. AI Winter":
    section_header("06", "AI Winter – شتاء الذكاء الاصطناعي",
                   "فترات تراجع التمويل والحماس بسبب عدم تحقق بعض التوقعات.")
    cols = st.columns(3)
    items = [
        ("Expectations", "توقعات مرتفعة", "وعود أسرع من قدرة التكنولوجيا."),
        ("Compute", "حوسبة محدودة", "المعالجة والذاكرة لم تكف لبعض الطموحات."),
        ("Data", "نقص البيانات", "لم تكن البيانات الرقمية متاحة بحجم اليوم."),
        ("Scale", "صعوبة التوسع", "نجاح نموذج صغير لا يعني نجاحه في الواقع."),
        ("Cost", "التكلفة", "بعض الأنظمة كانت مكلفة في التطوير والصيانة."),
        ("Trust", "فقدان الثقة", "تراجع دعم بعض الجهات عند عدم تحقق النتائج."),
    ]
    for i, item in enumerate(items):
        with cols[i % 3]:
            mini_card(*item)
    callout("AI Winter لا يعني أن البحث توقف تمامًا؛ بل أن التمويل والحماس انخفضا في فترات معينة.", "info")

elif selected == "7. Expert Systems":
    section_header("07", "Expert Systems – الأنظمة الخبيرة", "Knowledge-based systems")
    st.markdown("الهدف هو نقل معرفة خبير في مجال محدد إلى قاعدة معرفة، ثم استخدام محرك استدلال لتطبيق القواعد.")
    clean_table(["المكوّن", "الوظيفة"], [
        ["Knowledge Base", "حقائق وقواعد وخبرة المجال"],
        ["Inference Engine", "تطبيق القواعد للوصول إلى نتيجة"],
        ["User Interface", "التفاعل مع المستخدم"],
    ])
    callout("مثال: نظام لتقييم المخاطر المالية باستخدام عشرات أو مئات القواعد المأخوذة من خبراء.", "success")
    callout("المشكلة: تحديث آلاف القواعد صعب، والنظام لا يتعلم تلقائيًا من البيانات الجديدة مثل Machine Learning.", "warn")

elif selected == "8. Machine Learning":
    section_header("08", "Machine Learning", "من Programming Rules إلى Learning from Data")
    clean_table(["النهج", "كيف يعمل؟", "مثال"], [
        ["Rule-Based", "الإنسان يكتب القواعد", "خصم ثابت عند تجاوز قيمة شراء"],
        ["Machine Learning", "النموذج يتعلم من البيانات", "توقع Customer Churn"],
    ])
    callout("<strong>التحول المركزي:</strong> بدل أن نسأل «ما القواعد التي نكتبها؟» أصبح السؤال «ما الأنماط التي يستطيع النموذج تعلمها من البيانات؟».", "success")

elif selected == "9. Deep Learning":
    section_header("09", "Neural Networks وDeep Learning",
                   "عودة قوية للشبكات العصبية في العقد الثاني من القرن الحادي والعشرين.")
    cols = st.columns(4)
    for col, item in zip(cols, [
        ("Big Data", "البيانات", "أمثلة تدريب أكثر."),
        ("GPU", "الحوسبة", "تسريع التدريب."),
        ("Algorithms", "الخوارزميات", "تقنيات تدريب وبنى أفضل."),
        ("Software", "الأدوات", "مكتبات جعلت التطوير أسهل."),
    ]):
        with col:
            mini_card(*item)
    callout("Deep Learning يعتمد على شبكات عصبية متعددة الطبقات تتعلم تمثيلات معقدة من البيانات.", "info")
    st.markdown("أدى إلى تقدم كبير في الصور والصوت والنص، ومهد لمرحلة جديدة من AI.")

elif selected == "10. محطات التطور الحديث":
    section_header("10", "محطات مفصلية في التطور الحديث", "Selected milestones")
    clean_table(["السنة", "المحطة", "ماذا تعني؟"], [
        ["1997", "IBM Deep Blue", "إنجاز بارز في الشطرنج."],
        ["2012", "AlexNet", "رمز لقفزة Deep Learning في رؤية الحاسوب."],
        ["2016", "AlphaGo", "إنجاز مهم يجمع Deep Learning وReinforcement Learning."],
        ["2017", "Transformer", "بنية Attention أصبحت أساسًا لكثير من نماذج اللغة."],
        ["2020", "GPT-3", "قدرات Few-Shot على مهام لغوية متعددة."],
        ["2022+", "Generative AI", "انتشار واسع للنماذج الحوارية والتوليدية."],
    ])
    callout("هذه محطات تعليمية منتقاة وليست قائمة كاملة بكل إنجازات AI.", "warn")

elif selected == "11. Transformer - 2017":
    section_header("11", "Transformer – 2017", "Attention Is All You Need")
    callout("<strong>Attention:</strong> آلية تساعد النموذج على تحديد أجزاء السياق الأكثر صلة عند معالجة عنصر معين.", "success")
    clean_table(["قبل Transformer", "مع Transformer"], [
        ["اعتماد كبير على نماذج متتابعة مثل RNN/LSTM", "معالجة العلاقات بين العناصر بطريقة أكثر قابلية للتوازي"],
        ["صعوبات أكبر مع التسلسلات الطويلة", "أساس مناسب لبناء نماذج لغوية أكبر"],
    ])
    st.markdown("أهمية Transformer أنه أصبح بنية أساسية لكثير من Large Language Models الحديثة.")

elif selected == "12. Large Language Models":
    section_header("12", "Large Language Models", "النماذج اللغوية الكبيرة")
    st.markdown("تتعلم LLMs أنماط اللغة على نطاق واسع، ويمكنها تنفيذ مهام متعددة من خلال التعليمات والأمثلة داخل السياق.")
    cols = st.columns(2)
    for i, item in enumerate([
        ("Summarization", "التلخيص", "اختصار نص طويل."),
        ("Translation", "الترجمة", "التحويل بين اللغات."),
        ("Q&A", "الأسئلة والأجوبة", "الاستجابة للأسئلة ضمن السياق."),
        ("Drafting", "المسودات", "إعداد مسودة تقرير أو رسالة."),
    ]):
        with cols[i % 2]:
            mini_card(*item)
    callout("GPT-3 (2020) ارتبط تاريخيًا بإظهار Few-Shot capabilities: تنفيذ مهام من خلال أمثلة قليلة داخل النص.", "info")
    callout("LLM نموذج احتمالي؛ يمكن أن يخطئ أو يولد معلومات غير دقيقة، لذلك يحتاج إلى تحقق.", "warn")

elif selected == "13. RLHF واتباع التعليمات":
    section_header("13", "Instruction Following وRLHF",
                   "جعل النماذج أكثر ملاءمة لتعليمات المستخدم.")
    st.markdown("""
    <div class="flow">
        <div class="flow-step"><div class="n">1</div><b>Human examples</b><small>أمثلة للسلوك المرغوب</small></div>
        <div class="flow-step"><div class="n">2</div><b>Rank outputs</b><small>ترتيب إجابات مختلفة</small></div>
        <div class="flow-step"><div class="n">3</div><b>Reward model</b><small>تعلم التفضيلات</small></div>
        <div class="flow-step"><div class="n">4</div><b>Improve model</b><small>تحسين الاستجابة</small></div>
    </div>
    """, unsafe_allow_html=True)
    callout("<strong>RLHF:</strong> Reinforcement Learning from Human Feedback – استخدام تغذية راجعة بشرية لتحسين سلوك النموذج.", "success")

elif selected == "14. Generative AI":
    section_header("14", "Generative AI", "من التنبؤ إلى التوليد")
    clean_table(["المهمة", "المخرج", "مثال"], [
        ["Prediction", "احتمال/قيمة", "توقع المبيعات"],
        ["Classification", "فئة", "طبيعي/مشبوه"],
        ["Generation", "محتوى جديد", "نص أو صورة أو صوت أو كود"],
    ])
    cols = st.columns(3)
    for col, item in zip(cols, [
        ("Text", "النص", "تقارير، تلخيص، رسائل."),
        ("Image", "الصورة", "تصميمات وصور مولدة."),
        ("Audio/Video", "الصوت والفيديو", "محتوى وسائط متعدد الأنماط."),
    ]):
        with col:
            mini_card(*item)
    callout("Generative AI لا يلغي Prediction أو Classification؛ بل يضيف نوعًا جديدًا من المخرجات.", "info")

elif selected == "15. AI في المؤسسة عبر الزمن":
    section_header("15", "AI في المؤسسة عبر الزمن", "كيف تغيرت القيمة الإدارية؟")
    clean_table(["المرحلة", "الاستخدام المؤسسي", "مثال"], [
        ["Expert Systems", "قواعد خبيرة لقرار محدد", "تقييم مخاطر"],
        ["Machine Learning", "تنبؤ وتصنيف", "توقع الطلب / Churn"],
        ["Deep Learning", "تحليل بيانات غير مهيكلة", "صور، صوت، نص"],
        ["Generative AI", "دعم العمل المعرفي", "تلخيص، مسودات، تحليل وثائق"],
    ])
    callout("<strong>درس استراتيجي:</strong> الأداة وحدها لا تكفي. تحتاج المؤسسة بيانات وبنية تحتية ومهارات وحوكمة وHuman Oversight.", "success")

elif selected == "16. TD وQuiz":
    section_header("16", "TD وQuiz", "اختبر قدرتك على ترتيب الأحداث وفهم الانتقالات.")
    st.markdown("### نشاط سريع")
    callout("رتب: Transformer – Dartmouth – GPT-3 – Turing – Expert Systems – Deep Learning – Generative AI – Machine Learning.", "info")
    with st.expander("إظهار ترتيب مقترح"):
        st.markdown("Turing (1950) → Dartmouth (1956) → Expert Systems → Machine Learning → Deep Learning → Transformer (2017) → GPT-3 (2020) → Generative AI.")
    st.markdown("### Quiz")
    questions = [
        ("1) سنة نشر مقال Turing؟", ["1950", "1956", "2017"], "1950"),
        ("2) Dartmouth يرتبط أساسًا بـ:", ["تسمية وتنظيم مجال AI", "Transformer", "Deep Learning"], "تسمية وتنظيم مجال AI"),
        ("3) Symbolic AI يعتمد على:", ["Rules & Logic", "صور فقط", "لا بيانات ولا قواعد"], "Rules & Logic"),
        ("4) AI Winter يعني:", ["تراجع الحماس والتمويل", "توقف الإنترنت", "ظهور GenAI"], "تراجع الحماس والتمويل"),
        ("5) ML يعني أن النموذج:", ["يتعلم من البيانات", "يحتاج قواعد بشرية فقط", "لا يستخدم خوارزميات"], "يتعلم من البيانات"),
        ("6) Transformer اشتهر سنة:", ["2017", "1950", "1980"], "2017"),
        ("7) RLHF =", ["Reinforcement Learning from Human Feedback", "Rule Logic Hardware Function", "لا شيء"], "Reinforcement Learning from Human Feedback"),
        ("8) Generative AI يركز على:", ["توليد محتوى جديد", "الحساب اليدوي", "التخزين فقط"], "توليد محتوى جديد"),
    ]
    with st.form("quiz2"):
        answers = []
        for q, options, correct in questions:
            answers.append((st.radio(q, options, index=None), correct))
        submitted = st.form_submit_button("تصحيح")
    if submitted:
        score = sum(a == c for a, c in answers)
        if score >= 7:
            st.success(f"النتيجة: {score}/8 – ممتاز.")
        elif score >= 5:
            st.info(f"النتيجة: {score}/8 – جيد، راجع الخط الزمني.")
        else:
            st.warning(f"النتيجة: {score}/8 – راجع الأقسام الأساسية ثم أعد الاختبار.")

elif selected == "17. الخلاصة والمراجع":
    section_header("17", "الخلاصة والمراجع", "ما الذي يجب أن يبقى واضحًا بعد المحاضرة؟")
    clean_table(["المرحلة", "الفكرة الأساسية"], [
        ["1950 – Turing", "السؤال العلمي عن سلوك الآلة الذكي."],
        ["1956 – Dartmouth", "ترسيخ AI كحقل بحثي."],
        ["Symbolic AI / Expert Systems", "المعرفة في صورة قواعد."],
        ["Machine Learning", "التعلم من البيانات."],
        ["Deep Learning", "شبكات عميقة مدفوعة بالبيانات والحوسبة."],
        ["Transformer → LLMs → GenAI", "نماذج واسعة قادرة على التفاعل والتوليد."],
    ])
    callout("<strong>الجملة الكبرى:</strong> تاريخ AI هو انتقال من برمجة المعرفة كقواعد إلى التعلم من البيانات، ثم إلى نماذج عميقة وكبيرة قادرة على التعامل مع السياق وتوليد محتوى جديد.", "success")
    st.markdown("### مراجع أساسية")
    st.markdown("""
- Turing, A. M. (1950). *Computing Machinery and Intelligence*. Mind, 59(236), 433-460.
- McCarthy, J., Minsky, M. L., Rochester, N., & Shannon, C. E. (1955/2006). *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence*.
- Russell, S. J., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.).
- LeCun, Y., Bengio, Y., & Hinton, G. (2015). *Deep learning*. Nature, 521, 436-444.
- Vaswani, A., et al. (2017). *Attention Is All You Need*.
- Brown, T. B., et al. (2020). *Language Models are Few-Shot Learners*.
- Ouyang, L., et al. (2022). *Training language models to follow instructions with human feedback*.
""")
