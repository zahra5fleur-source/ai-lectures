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
def section_header(num, title, intro=None, kicker="المحاضرة الأولى"):
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
    "1. لماذا ندرس الذكاء الاصطناعي؟",
    "2. ما هو الذكاء الاصطناعي؟",
    "3. التقليدي أم الذكي؟",
    "4. لماذا تطور AI سريعًا؟",
    "5. ماذا يستطيع AI أن يفعل؟",
    "6. أبرز تقنيات AI",
    "7. AI و ML و DL",
    "8. AI في علوم التسيير",
    "9. البيانات واتخاذ القرار",
    "10. دراسة حالة: Customer Churn",
    "11. حدود AI والمسؤولية",
    "12. نشاط TD",
    "13. Quiz تفاعلي",
    "14. خلاصة المحاضرة",
    "15. المراجع",
]

with st.sidebar:
    st.markdown("## مقدمة في الذكاء الاصطناعي")
    st.markdown("**السنة الثانية ليسانس – علوم التسيير**")
    st.markdown("---")
    selected = st.radio("خريطة المحاضرة", sections, label_visibility="collapsed")
    idx = sections.index(selected)
    st.progress(idx / (len(sections)-1))
    st.caption(f"التقدم داخل المحاضرة: {idx}/{len(sections)-1}")
    st.markdown("---")
    st.markdown(
        """
        <div style="font-size:.85rem; line-height:1.8; color:#DCEBF4;">
        تصميم أكاديمي مبسط يركز على الفهم، الأمثلة الإدارية، والتفاعل.
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# HERO
# =========================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">المحاضرة 01</div>
        <h1>مقدمة في الذكاء الاصطناعي</h1>
        <p>
        مدخل مبسط لفهم مفهوم الذكاء الاصطناعي، قدراته الأساسية، أهم تقنياته،
        وكيف يمكن توظيفه في تحليل البيانات ودعم القرار داخل المؤسسات.
        </p>
        <div class="hero-meta">
            <span class="hero-chip">المستوى: السنة الثانية</span>
            <span class="hero-chip">التخصص: علوم التسيير</span>
            <span class="hero-chip">المقياس: Introduction to AI</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HOME
# =========================================================
if selected == "الرئيسية":
    section_header("00", "أهداف المحاضرة", "في نهاية هذه المحاضرة، يفترض أن يكون الطالب قادرًا على فهم الأساسيات دون الدخول في تفاصيل برمجية معقدة.")

    c1, c2, c3 = st.columns(3)
    with c1:
        mini_card("Understand", "فهم المفهوم", "تعريف الذكاء الاصطناعي وبيان موقعه ضمن العلوم الحديثة.")
    with c2:
        mini_card("Distinguish", "التمييز", "الفرق بين النظام التقليدي والنظام القائم على الذكاء الاصطناعي.")
    with c3:
        mini_card("Apply", "الربط بالتطبيق", "ربط AI بتحليل البيانات والتنبؤ والتوصية ودعم القرار الإداري.")

    c4, c5, c6 = st.columns(3)
    with c4:
        mini_card("Identify", "التعرّف على التقنيات", "Machine Learning وDeep Learning وNLP وGenerative AI.")
    with c5:
        mini_card("Analyze", "تحليل أمثلة", "التعرف على استخدامات AI في التسويق والمالية والموارد البشرية.")
    with c6:
        mini_card("Evaluate", "إدراك الحدود", "فهم أن AI أداة مساعدة ولا يلغي دور الإنسان في التحقق واتخاذ القرار.")

    callout(
        "<strong>الفكرة المركزية للمحاضرة:</strong> قيمة الذكاء الاصطناعي في الإدارة لا تأتي من التقنية وحدها، بل من قدرته على تحويل البيانات إلى تنبؤات وتوصيات تدعم قرارات أفضل.",
        "success",
    )

# =========================================================
# 1 WHY AI
# =========================================================
elif selected == "1. لماذا ندرس الذكاء الاصطناعي؟":
    section_header("01", "لماذا ندرس الذكاء الاصطناعي؟", "قبل التعريفات، نبدأ بسؤال بسيط: أين نلتقي بالذكاء الاصطناعي في حياتنا اليومية وفي المؤسسة؟")

    callout(
        "<strong>سؤال افتتاحي:</strong> هل الآلة الحاسبة، Excel، نظام توصية Netflix، ChatGPT، ونظام كشف الاحتيال كلها ذكاء اصطناعي؟",
        "info",
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        mini_card("Everyday Life", "في الحياة اليومية", "التوصيات، البحث الذكي، الترجمة، المساعدات الرقمية، وتوليد المحتوى.")
    with c2:
        mini_card("Organizations", "في المؤسسات", "تحليل العملاء، التنبؤ بالمبيعات، أتمتة العمليات، واكتشاف المخاطر.")
    with c3:
        mini_card("Decision Making", "في القرار", "تقديم تنبؤ أو توصية تساعد المدير على تقييم البدائل قبل اتخاذ القرار.")

    st.markdown("### لماذا يهم طالب علوم التسيير؟")
    clean_table(
        ["المجال", "كيف يساعد AI؟", "مثال مبسط"],
        [
            ["التسويق", "فهم العملاء والتخصيص", "اقتراح عرض مناسب لكل عميل"],
            ["المالية", "التنبؤ والمخاطر", "تقدير احتمال التعثر"],
            ["الموارد البشرية", "تحليل البيانات", "رصد أنماط الغياب أو الدوران"],
            ["المحاسبة", "اكتشاف الأنماط غير العادية", "رصد معاملات تحتاج مراجعة"],
            ["الإدارة", "دعم القرار", "مقارنة السيناريوهات والبدائل"],
        ],
    )

# =========================================================
# 2 WHAT IS AI
# =========================================================
elif selected == "2. ما هو الذكاء الاصطناعي؟":
    section_header("02", "ما هو الذكاء الاصطناعي؟", "لا يوجد تعريف واحد جامع، لكن التعريفات الحديثة تركز على قدرة النظام على معالجة المدخلات وتوليد مخرجات مفيدة بصورة تتسم بدرجات من الاستقلالية.")

    callout(
        "<strong>تعريف مبسط:</strong> الذكاء الاصطناعي هو مجموعة من الأساليب والأنظمة الحاسوبية التي تمكّن الآلة من تنفيذ مهام ترتبط عادةً بقدرات بشرية مثل التعلّم، التنبؤ، التصنيف، التعرف، التوصية، وتوليد المحتوى.",
        "success",
    )

    st.markdown("### عناصر الفكرة")
    cols = st.columns(4)
    cards = [
        ("Input", "مدخلات", "بيانات، نصوص، صور، صوت أو إشارات."),
        ("Inference", "استدلال", "استخلاص نمط أو علاقة من المدخلات."),
        ("Output", "مخرجات", "تنبؤ، قرار، توصية أو محتوى."),
        ("Autonomy", "استقلالية نسبية", "قد يعمل النظام بدرجات مختلفة من التدخل البشري."),
    ]
    for col, (en, ar, desc) in zip(cols, cards):
        with col:
            mini_card(en, ar, desc)

    st.markdown("### هل كل برنامج حاسوبي ذكاءً اصطناعيًا؟")
    callout(
        "لا. البرنامج الذي ينفذ قواعد ثابتة فقط قد يكون مفيدًا جدًا، لكنه لا يُصنف بالضرورة على أنه نظام ذكاء اصطناعي. المهم هو طبيعة المهمة وكيف تُنتج المخرجات.",
        "warn",
    )

# =========================================================
# 3 TRADITIONAL VS AI
# =========================================================
elif selected == "3. التقليدي أم الذكي؟":
    section_header("03", "النظام التقليدي أم النظام الذكي؟", "الفارق الأساسي لا يتعلق بواجهة البرنامج، بل بطريقة تحويل المدخلات إلى مخرجات.")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="compare-box traditional">
                <div class="compare-title">النظام التقليدي</div>
                <ul>
                    <li>يعتمد غالبًا على قواعد يضعها المبرمج مسبقًا.</li>
                    <li>نفس القاعدة تعطي نفس السلوك.</li>
                    <li>لا يتعلم تلقائيًا من البيانات.</li>
                    <li>مناسب للمهام المستقرة والواضحة.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="compare-box ai">
                <div class="compare-title">النظام القائم على AI</div>
                <ul>
                    <li>قد يتعلم أنماطًا من البيانات.</li>
                    <li>يعالج حالات جديدة بناءً على ما تعلمه.</li>
                    <li>قد ينتج احتمالات أو تنبؤات بدل قاعدة ثابتة.</li>
                    <li>مناسب للمهام المعقدة والمتغيرة.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### مثال إداري")
    clean_table(
        ["المهمة", "حل تقليدي", "حل قائم على AI"],
        [
            ["منح تخفيض", "إذا تجاوزت المشتريات قيمة محددة → خصم", "نموذج يتوقع حساسية العميل للسعر"],
            ["تصنيف بريد", "قائمة كلمات ثابتة", "نموذج يتعلم من آلاف الرسائل"],
            ["توقع المبيعات", "متوسطات ومعادلات ثابتة", "نموذج يتعلم من تاريخ المبيعات ومتغيرات أخرى"],
        ],
    )

# =========================================================
# 4 WHY FAST
# =========================================================
elif selected == "4. لماذا تطور AI سريعًا؟":
    section_header("04", "لماذا تطور الذكاء الاصطناعي بسرعة؟", "تقدم AI لم يحدث بسبب عامل واحد، بل نتيجة تفاعل عدة عوامل تقنية واقتصادية.")

    cols = st.columns(4)
    items = [
        ("Data", "البيانات", "تزايد البيانات الرقمية التي يمكن استخدامها في التدريب والتحليل."),
        ("Compute", "القدرة الحاسوبية", "تطور المعالجات والخدمات السحابية خفّض زمن التدريب والتشغيل."),
        ("Algorithms", "الخوارزميات", "تحسن أساليب التعلم والنماذج العصبية والتمثيلات."),
        ("Connectivity", "الاتصال", "الإنترنت والحوسبة السحابية سهّلا الوصول إلى البيانات والنماذج."),
    ]
    for col, item in zip(cols, items):
        with col:
            mini_card(*item)

    callout(
        "<strong>قاعدة مهمة:</strong> لا يكفي امتلاك بيانات كثيرة. القيمة تظهر عندما تكون البيانات مناسبة، والخوارزمية ملائمة، والهدف الإداري واضحًا.",
        "success",
    )

# =========================================================
# 5 CAPABILITIES
# =========================================================
elif selected == "5. ماذا يستطيع AI أن يفعل؟":
    section_header("05", "ماذا يستطيع الذكاء الاصطناعي أن يفعل؟", "من الأفضل فهم AI من خلال نوع المهمة التي ينجزها بدل حفظ أسماء الأدوات.")

    cols = st.columns(3)
    features = [
        ("Prediction", "التنبؤ", "ماذا قد يحدث؟ مثال: توقع المبيعات."),
        ("Classification", "التصنيف", "إلى أي فئة ينتمي؟ مثال: معاملة طبيعية أو مشبوهة."),
        ("Recommendation", "التوصية", "ما الخيار الأنسب؟ مثال: منتج مناسب للعميل."),
        ("Generation", "التوليد", "إنتاج نص أو صورة أو ملخص أو فكرة أولية."),
        ("Recognition", "التعرّف", "اكتشاف كائن أو نمط داخل صورة أو صوت أو بيانات."),
        ("Decision Support", "دعم القرار", "تجميع الأدلة والتنبؤات لتقوية قرار المدير."),
    ]
    for i, item in enumerate(features):
        with cols[i % 3]:
            mini_card(*item)

    clean_table(
        ["الوظيفة", "السؤال الذي تجيب عنه", "مثال إداري"],
        [
            ["Prediction | التنبؤ", "ماذا قد يحدث؟", "توقع المبيعات"],
            ["Classification | التصنيف", "إلى أي فئة ينتمي؟", "عملية بنكية طبيعية/مشبوهة"],
            ["Recommendation | التوصية", "ماذا نقترح؟", "منتج مناسب للعميل"],
            ["Generation | التوليد", "هل يمكن إنتاج محتوى؟", "مسودة تقرير أو إعلان"],
            ["Recognition | التعرّف", "ما الموجود هنا؟", "كشف عيب في منتج"],
            ["Decision Support | دعم القرار", "ما المعلومات التي يحتاجها المدير؟", "تقدير مخاطر الاستثمار"],
        ],
    )

# =========================================================
# 6 TECHNIQUES
# =========================================================
elif selected == "6. أبرز تقنيات AI":
    section_header("06", "أبرز تقنيات الذكاء الاصطناعي", "هذه التقنيات ليست متساوية ولا منفصلة تمامًا؛ بعضها يقع داخل بعض، وبعضها يخدم نوعًا معينًا من البيانات أو المهام.")

    c1, c2, c3 = st.columns(3)
    with c1:
        mini_card("Machine Learning", "التعلم الآلي", "تعلم الأنماط من البيانات لإجراء تنبؤ أو تصنيف أو توصية.")
    with c2:
        mini_card("Deep Learning", "التعلم العميق", "نوع من التعلم الآلي يعتمد على شبكات عصبية متعددة الطبقات.")
    with c3:
        mini_card("NLP", "معالجة اللغة الطبيعية", "تحليل وفهم وتوليد اللغة البشرية.")

    c4, c5, c6 = st.columns(3)
    with c4:
        mini_card("Computer Vision", "الرؤية الحاسوبية", "تحليل الصور والفيديو والتعرف على العناصر والأنماط.")
    with c5:
        mini_card("Expert Systems", "الأنظمة الخبيرة", "محاكاة قواعد ومعرفة خبير في مجال محدد.")
    with c6:
        mini_card("Generative AI", "الذكاء الاصطناعي التوليدي", "إنشاء محتوى جديد مثل النص والصورة والصوت والبرمجيات.")

    callout(
        "في هذا المقياس سنركز على الفهم المفاهيمي والتطبيق الإداري، وليس على التفاصيل الرياضية أو البرمجية العميقة.",
        "info",
    )

# =========================================================
# 7 AI ML DL
# =========================================================
elif selected == "7. AI و ML و DL":
    section_header("07", "العلاقة بين AI و ML و DL", "خطأ شائع هو استخدام هذه المصطلحات كما لو كانت مترادفات.")

    st.markdown(
        """
        <div class="hierarchy">
            <div class="layer ai-layer">Artificial Intelligence — الذكاء الاصطناعي
                <span>المجال الأوسع: أنظمة تنجز مهام ترتبط بالذكاء</span>
            </div>
            <div class="layer ml-layer">Machine Learning — التعلم الآلي
                <span>جزء من AI يتعلم من البيانات</span>
            </div>
            <div class="layer dl-layer">Deep Learning — التعلم العميق
                <span>جزء من ML يعتمد على الشبكات العصبية العميقة</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    callout(
        "<strong>العلاقة المختصرة:</strong> Deep Learning ⊂ Machine Learning ⊂ Artificial Intelligence.",
        "success",
    )
    callout(
        "لكن ليس كل AI هو Machine Learning؛ فالأنظمة الخبيرة القائمة على قواعد واضحة مثال على AI لا يعتمد بالضرورة على التعلم من البيانات.",
        "warn",
    )

# =========================================================
# 8 MANAGEMENT
# =========================================================
elif selected == "8. AI في علوم التسيير":
    section_header("08", "الذكاء الاصطناعي في علوم التسيير", "نربط الآن المفهوم بالوظائف الأساسية داخل المؤسسة.")

    clean_table(
        ["الوظيفة الإدارية", "أمثلة استخدام AI", "القيمة المحتملة"],
        [
            ["التسويق", "تقسيم العملاء، التوصية، تحليل التعليقات", "تخصيص أفضل وفهم أدق للسوق"],
            ["المالية", "التنبؤ، تقييم المخاطر، اكتشاف الاحتيال", "قرارات مالية أسرع وأكثر اتساقًا"],
            ["الموارد البشرية", "تحليل المهارات، توقع الدوران، دعم التوظيف", "استخدام أفضل لبيانات الموارد البشرية"],
            ["المحاسبة", "مطابقة المعاملات، كشف الشذوذ، أتمتة أولية", "تقليل المهام المتكررة ودعم المراجعة"],
            ["الإنتاج والعمليات", "توقع الطلب، الصيانة التنبؤية، تحسين الجدولة", "خفض التوقف والهدر"],
            ["الإدارة العليا", "لوحات ذكية، سيناريوهات، دعم القرار", "رؤية أشمل قبل اتخاذ القرار"],
        ],
    )

    c1, c2 = st.columns(2)
    with c1:
        callout(
            "<strong>Automation — الأتمتة:</strong> تنفيذ مهمة متكررة بسرعة واتساق.",
            "info",
        )
    with c2:
        callout(
            "<strong>Augmentation — التعزيز:</strong> مساعدة الإنسان على اتخاذ قرار أفضل دون إلغاء دوره.",
            "success",
        )

# =========================================================
# 9 DATA + DECISION
# =========================================================
elif selected == "9. البيانات واتخاذ القرار":
    section_header("09", "AI وتحليل البيانات واتخاذ القرار", "ليس كل تحليل بيانات ذكاءً اصطناعيًا، لكن AI يمكن أن يضيف طبقة تنبؤية أو توصياتية فوق التحليل التقليدي.")

    st.markdown("### مستويات التحليل")
    clean_table(
        ["المستوى", "السؤال", "مثال"],
        [
            ["Descriptive | وصفي", "ماذا حدث؟", "المبيعات انخفضت 8%"],
            ["Diagnostic | تشخيصي", "لماذا حدث؟", "الانخفاض تركز في منطقة محددة"],
            ["Predictive | تنبؤي", "ماذا قد يحدث؟", "توقع مبيعات الشهر القادم"],
            ["Prescriptive | توجيهي", "ماذا نفعل؟", "اقتراح أفضل إجراء أو بديل"],
        ],
    )

    st.markdown("### من البيانات إلى القرار")
    st.markdown(
        """
        <div class="flow">
            <div class="flow-step"><div class="n">1</div><b>Data</b><small>بيانات المؤسسة</small></div>
            <div class="flow-step"><div class="n">2</div><b>Analysis</b><small>تنظيف وتحليل</small></div>
            <div class="flow-step"><div class="n">3</div><b>AI Model</b><small>نمط أو نموذج</small></div>
            <div class="flow-step"><div class="n">4</div><b>Prediction</b><small>تنبؤ أو توصية</small></div>
            <div class="flow-step"><div class="n">5</div><b>Manager</b><small>تفسير وسياق</small></div>
            <div class="flow-step"><div class="n">6</div><b>Decision</b><small>القرار النهائي</small></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    callout(
        "<strong>المدير يبقى في الحلقة:</strong> النموذج يقدم معلومات، لكن القرار يحتاج أهداف المؤسسة والسياق والخبرة والمسؤولية.",
        "success",
    )

# =========================================================
# 10 CASE
# =========================================================
elif selected == "10. دراسة حالة: Customer Churn":
    section_header("10", "دراسة حالة مبسطة: Customer Churn", "كيف نترجم مشكلة إدارية إلى سؤال يمكن للذكاء الاصطناعي المساعدة في الإجابة عنه؟")

    callout(
        "<strong>المشكلة:</strong> شركة لديها 50,000 عميل وتلاحظ أن بعضهم يتوقف عن الشراء أو يترك الخدمة. الإدارة تريد معرفة العملاء الأكثر عرضة للمغادرة.",
        "info",
    )

    st.markdown(
        """
        <div class="flow">
            <div class="flow-step"><div class="n">1</div><b>السؤال الإداري</b><small>من قد يغادر؟</small></div>
            <div class="flow-step"><div class="n">2</div><b>البيانات</b><small>الشراء، الشكاوى، الاستخدام...</small></div>
            <div class="flow-step"><div class="n">3</div><b>النموذج</b><small>يتعلم من حالات سابقة</small></div>
            <div class="flow-step"><div class="n">4</div><b>النتيجة</b><small>احتمال مغادرة لكل عميل</small></div>
            <div class="flow-step"><div class="n">5</div><b>الإجراء</b><small>عرض احتفاظ أو تواصل</small></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    clean_table(
        ["نوع البيانات", "مثال", "لماذا قد يكون مهمًا؟"],
        [
            ["بيانات المعاملات", "عدد المشتريات وقيمتها", "تعكس نشاط العميل"],
            ["بيانات الخدمة", "عدد الشكاوى", "قد تشير إلى عدم الرضا"],
            ["بيانات الاستخدام", "تراجع الدخول أو الاستعمال", "قد يسبق قرار المغادرة"],
            ["بيانات زمنية", "مدة العلاقة مع المؤسسة", "توضح مرحلة العلاقة"],
        ],
    )

    callout(
        "<strong>المهم:</strong> النموذج لا «يعرف» العميل كما يعرفه الإنسان. هو يتعلم علاقات إحصائية من البيانات ويعطي درجة أو احتمالًا يحتاج إلى تفسير.",
        "warn",
    )

# =========================================================
# 11 LIMITS
# =========================================================
elif selected == "11. حدود AI والمسؤولية":
    section_header("11", "حدود الذكاء الاصطناعي والمسؤولية", "الاستفادة من AI تتطلب فهم ما يستطيع فعله وما لا ينبغي الاعتماد عليه فيه دون تحقق.")

    c1, c2, c3 = st.columns(3)
    with c1:
        mini_card("Data Quality", "جودة البيانات", "البيانات الناقصة أو المنحازة قد تنتج نتائج ضعيفة أو مضللة.")
    with c2:
        mini_card("Bias", "التحيز", "النموذج قد يعكس أنماطًا غير عادلة موجودة في البيانات.")
    with c3:
        mini_card("Errors", "الأخطاء", "النماذج قد تقدم إجابة غير صحيحة أو غير مناسبة للسياق.")

    c4, c5, c6 = st.columns(3)
    with c4:
        mini_card("Privacy", "الخصوصية", "يجب حماية البيانات الشخصية والحساسة وعدم استخدامها عشوائيًا.")
    with c5:
        mini_card("Transparency", "الشفافية", "ينبغي فهم مصدر النتيجة وحدودها بقدر الإمكان.")
    with c6:
        mini_card("Human Oversight", "الرقابة البشرية", "المستخدم مسؤول عن المراجعة والسياق والقرار النهائي.")

    callout(
        "<strong>قاعدة العمل:</strong> استخدم AI كمساعد في التفكير والتحليل، لا كبديل عن التحقق والخبرة والمسؤولية.",
        "danger",
    )

# =========================================================
# 12 TD
# =========================================================
elif selected == "12. نشاط TD":
    section_header("12", "نشاط تطبيقي TD", "النشاط يركز على التمييز بين البرامج التقليدية واستخدامات AI، ثم ربط كل حالة بنوع المهمة.")

    st.markdown("### النشاط 1 — هل هذا AI؟")
    clean_table(
        ["الحالة", "مهمتك"],
        [
            ["Excel يحسب SUM لمجموعة أرقام", "AI أم برنامج تقليدي؟ ولماذا؟"],
            ["نظام يقترح منتجات بناءً على تاريخ الشراء", "AI أم برنامج تقليدي؟ وما نوع المهمة؟"],
            ["ChatGPT يلخص تقريرًا", "ما نوع القدرة المستخدمة؟"],
            ["قاعدة: إذا تجاوزت المشتريات 10000 دج امنح 5% خصمًا", "AI أم قاعدة تقليدية؟"],
            ["نظام يتعلم من معاملات سابقة لاكتشاف الاحتيال", "ما نوع المهمة؟"],
        ],
    )

    with st.expander("إظهار التصحيح المقترح"):
        st.markdown(
            """
            1. **Excel SUM:** برنامج تقليدي؛ ينفذ عملية حسابية محددة.
            2. **اقتراح المنتجات:** AI؛ غالبًا Recommendation.
            3. **تلخيص التقرير:** Generative AI / NLP.
            4. **قاعدة الخصم:** منطق ثابت، وليس تعلمًا آليًا.
            5. **كشف الاحتيال:** غالبًا Classification أو Anomaly Detection.
            """
        )

    st.markdown("### النشاط 2 — من المشكلة إلى القرار")
    callout(
        "اختر مشكلة إدارية بسيطة من التسويق أو الموارد البشرية أو المالية، ثم حدد: البيانات المتاحة → السؤال → وظيفة AI المناسبة → المخرج → من يتخذ القرار النهائي.",
        "success",
    )

# =========================================================
# 13 QUIZ
# =========================================================
elif selected == "13. Quiz تفاعلي":
    section_header("13", "Quiz تفاعلي", "اختبار قصير للتأكد من استيعاب المفاهيم الأساسية.")

    with st.form("quiz_form"):
        q1 = st.radio(
            "1) أي عبارة تصف الذكاء الاصطناعي بصورة أفضل؟",
            ["أي برنامج يعمل على الحاسوب", "أنظمة تنفذ مهامًا مثل التعلم والتنبؤ والتوصية", "قاعدة بيانات كبيرة فقط"],
            index=None,
        )
        q2 = st.radio(
            "2) هل كل تحليل بيانات يُعد ذكاءً اصطناعيًا؟",
            ["نعم", "لا"],
            index=None,
        )
        q3 = st.radio(
            "3) ما العلاقة الصحيحة؟",
            ["AI جزء من ML", "ML جزء من AI", "لا توجد علاقة بينهما"],
            index=None,
        )
        q4 = st.radio(
            "4) توقع مغادرة العميل Customer Churn هو مثال أقرب إلى:",
            ["Classification / Prediction", "Generation", "Computer Vision فقط"],
            index=None,
        )
        q5 = st.radio(
            "5) في القرار الإداري، الدور الأنسب للذكاء الاصطناعي هو:",
            ["إلغاء دور المدير", "تقديم تنبؤات وتوصيات تدعم القرار", "اتخاذ كل القرارات دون رقابة"],
            index=None,
        )

        submitted = st.form_submit_button("تصحيح الاختبار")

    if submitted:
        answers = [
            (q1, "أنظمة تنفذ مهامًا مثل التعلم والتنبؤ والتوصية"),
            (q2, "لا"),
            (q3, "ML جزء من AI"),
            (q4, "Classification / Prediction"),
            (q5, "تقديم تنبؤات وتوصيات تدعم القرار"),
        ]
        score = sum(1 for user_answer, correct in answers if user_answer == correct)
        if score >= 4:
            st.success(f"النتيجة: {score}/5 — ممتاز. المفاهيم الأساسية واضحة.")
        elif score == 3:
            st.info(f"النتيجة: {score}/5 — جيد. راجع العلاقة بين المفاهيم ووظائف AI.")
        else:
            st.warning(f"النتيجة: {score}/5 — يُفضل مراجعة الأقسام 2 و5 و7 و9.")

# =========================================================
# 14 SUMMARY
# =========================================================
elif selected == "14. خلاصة المحاضرة":
    section_header("14", "خلاصة المحاضرة", "نراجع الأفكار التي يجب أن تبقى واضحة قبل الانتقال إلى المحاضرة الثانية.")

    st.markdown(
        """
        <div class="timeline-item"><b>1. AI مجال واسع</b><p>يشمل أنظمة تنجز مهامًا مثل التنبؤ والتصنيف والتوصية والتوليد ودعم القرار.</p></div>
        <div class="timeline-item"><b>2. ليس كل برنامج AI</b><p>هناك فرق بين القواعد الثابتة والأنظمة التي تستنتج أو تتعلم من البيانات.</p></div>
        <div class="timeline-item"><b>3. ML جزء من AI</b><p>وDeep Learning جزء من Machine Learning.</p></div>
        <div class="timeline-item"><b>4. البيانات عنصر أساسي</b><p>لكن جودتها وملاءمتها للهدف أهم من كثرتها فقط.</p></div>
        <div class="timeline-item"><b>5. القيمة الإدارية في دعم القرار</b><p>التنبؤ والتوصية والأتمتة تساعد المؤسسة على العمل بصورة أفضل.</p></div>
        <div class="timeline-item"><b>6. الإنسان يبقى مسؤولًا</b><p>يجب مراجعة النتائج وفهم السياق ومراعاة الخصوصية والتحيز والمخاطر.</p></div>
        """,
        unsafe_allow_html=True,
    )

    callout(
        "<strong>الجملة التي نغادر بها المحاضرة:</strong> الذكاء الاصطناعي لا يساوي «آلة تفكر مثل الإنسان»، بل مجموعة من الأنظمة التي تستخدم البيانات والخوارزميات لإنتاج مخرجات تساعد في أداء مهام محددة.",
        "success",
    )

# =========================================================
# 15 REFERENCES
# =========================================================
elif selected == "15. المراجع":
    section_header("15", "مراجع المحاضرة", "مراجع أساسية وحديثة نسبيًا يمكن الرجوع إليها لتوسيع المفاهيم الواردة في المحاضرة.")

    st.markdown(
        """
        <div class="card">
        <h3>مراجع أساسية</h3>
        <p>
        <b>Russell, S. J., & Norvig, P.</b> (2020). <i>Artificial Intelligence: A Modern Approach</i> (4th ed.). Pearson.
        </p><br>
        <p>
        <b>OECD.</b> (2024). <i>Explanatory memorandum on the updated OECD definition of an AI system</i>. OECD Artificial Intelligence Papers, No. 8.
        </p><br>
        <p>
        <b>Borges, A. F. S., Laurindo, F. J. B., Spínola, M. M., Gonçalves, R. F., & Mattos, C. A.</b> (2021).
        The strategic use of artificial intelligence in the digital era: Systematic literature review and future research directions.
        <i>International Journal of Information Management, 57</i>, 102225.
        </p><br>
        <p>
        <b>Jarrahi, M. H.</b> (2018). Artificial intelligence and the future of work: Human-AI symbiosis in organizational decision making.
        <i>Business Horizons, 61</i>(4), 577–586.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="source-note">ملاحظة: هذه المحاضرة تمهيدية؛ سيتم التوسع لاحقًا في أنواع AI، Machine Learning، النماذج اللغوية الكبيرة، Prompt Engineering، والأخلاقيات.</div>',
        unsafe_allow_html=True,
    )
