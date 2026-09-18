
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="المحاضرة 1 | مقدمة في الذكاء الاصطناعي",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------
# RTL + visual style
# ---------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
}
.block-container {
    padding-top: 1.4rem;
    padding-bottom: 3rem;
}
h1, h2, h3, h4 { direction: rtl; text-align: right; }
div[data-testid="stSidebar"] * { direction: rtl; text-align: right; }

.hero {
    border-radius: 22px;
    padding: 28px 34px;
    background: linear-gradient(135deg, rgba(33,91,173,.14), rgba(35,180,150,.10));
    border: 1px solid rgba(70,120,180,.18);
    margin-bottom: 18px;
}
.hero h1 {margin:0 0 8px 0; font-size: 2.15rem;}
.hero p {font-size: 1.05rem; margin: 0.35rem 0;}

.card-grid {
    display:grid;
    grid-template-columns: repeat(3, minmax(0,1fr));
    gap:14px;
    margin: 14px 0;
}
.card {
    border:1px solid rgba(120,120,120,.22);
    border-radius:18px;
    padding:16px;
    background:rgba(255,255,255,.72);
    box-shadow:0 2px 12px rgba(0,0,0,.04);
}
.card h4 {margin:0 0 8px 0;}
@media (max-width: 900px) {
    .card-grid { grid-template-columns:1fr; }
}

.flow {
    display:flex;
    align-items:center;
    justify-content:center;
    gap:8px;
    flex-wrap:wrap;
    margin:18px 0;
}
.flow .node {
    min-width: 130px;
    padding: 12px 14px;
    border-radius: 14px;
    background: rgba(66,133,244,.10);
    border: 1px solid rgba(66,133,244,.22);
    text-align:center;
    font-weight:700;
}
.flow .arrow {font-size:1.6rem; opacity:.65;}

.compare {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:16px;
    margin: 14px 0;
}
.compare .box {
    border-radius:18px;
    padding:18px;
    border:1px solid rgba(120,120,120,.22);
}
@media (max-width: 800px) {
    .compare {grid-template-columns:1fr;}
}

.note {
    border-right: 5px solid #4f83cc;
    padding: 10px 14px;
    background: rgba(79,131,204,.08);
    border-radius: 8px;
    margin: 12px 0;
}
.small {font-size:.90rem; opacity:.82;}
</style>
""", unsafe_allow_html=True)

sections = [
    "🏠 البداية وأهداف التعلم",
    "1️⃣ لماذا ندرس الذكاء الاصطناعي؟",
    "2️⃣ ما هو الذكاء الاصطناعي؟",
    "3️⃣ ماذا يستطيع AI أن يفعل؟",
    "4️⃣ هل كل برنامج حاسوبي AI؟",
    "5️⃣ النظام التقليدي وAI",
    "6️⃣ أبرز تقنيات AI",
    "7️⃣ AI في علوم التسيير",
    "8️⃣ AI وتحليل البيانات والقرار",
    "9️⃣ دراسة حالة: Customer Churn",
    "📝 Quiz تفاعلي",
    "👥 نشاط TD",
    "📚 المراجع",
]

with st.sidebar:
    st.title("مقدمة في الذكاء الاصطناعي")
    st.caption("السنة الثانية علوم التسيير")
    choice = st.radio("التنقل بين أجزاء المحاضرة", sections)
    st.divider()
    st.info("لا تفترض المحاضرة أي معرفة مسبقة بالبرمجة أو الذكاء الاصطناعي.")
    st.caption("المحاضرة مبنية على البرنامج الرسمي للمقياس ومراجع أكاديمية/مؤسسية مختارة.")

# ---------------------------
# Header
# ---------------------------
st.markdown("""
<div class="hero">
  <h1>المحاضرة الأولى: مقدمة في الذكاء الاصطناعي وأهميته</h1>
  <p><b>Introduction to Artificial Intelligence</b></p>
  <p>نسخة تعليمية مبسطة وموجهة لطلبة السنة الثانية علوم التسيير.</p>
</div>
""", unsafe_allow_html=True)

if choice == sections[0]:
    st.subheader("أهداف التعلم")
    st.write("بنهاية المحاضرة ينبغي أن يكون الطالب قادرًا على:")
    st.markdown("""
- تعريف الذكاء الاصطناعي **Artificial Intelligence (AI)** بصورة مبسطة.
- التمييز بين الأتمتة **Automation** والذكاء الاصطناعي.
- التعرف على أهم قدرات وتقنيات AI.
- فهم العلاقة بين **AI → Machine Learning → Deep Learning**.
- ذكر تطبيقات AI في التسويق والمالية والموارد البشرية والمحاسبة والعمليات.
- تفسير الدور الذي يؤديه AI في تحليل البيانات ودعم القرار.
- إدراك أن المخرجات الذكية تحتاج إلى تقييم وسياق ومسؤولية بشرية.
""")
    st.subheader("سؤال تمهيدي")
    st.write("هل الآلة الحاسبة وExcel وChatGPT ونظام كشف الاحتيال البنكي كلها أنظمة ذكاء اصطناعي؟")
    ans = st.radio("اختر الإجابة الأقرب:", [
        "نعم، كلها ذكاء اصطناعي.",
        "لا، ليست كلها ذكاء اصطناعي.",
        "لا أعرف بعد."
    ], key="warmup")
    if ans == "لا، ليست كلها ذكاء اصطناعي.":
        st.success("ممتاز. سنفهم لماذا خلال المحاضرة.")
    elif ans == "نعم، كلها ذكاء اصطناعي.":
        st.warning("هذه إجابة شائعة، لكن وجود برنامج حاسوبي لا يعني بالضرورة وجود AI.")
    else:
        st.info("لا مشكلة. هذا هو الهدف من المحاضرة.")

elif choice == sections[1]:
    st.subheader("1. لماذا ندرس الذكاء الاصطناعي؟")
    st.write(
        "أصبح الذكاء الاصطناعي جزءًا من العمل المؤسسي الحديث: في التحليل، التنبؤ، "
        "التسويق، الخدمات المالية، خدمة العملاء، والتعليم والصحة."
    )

    # Source-derived current statistic
    st.markdown('<div class="note"><b>سياق حديث:</b> يشير AI Index 2026 إلى أن 88% من المؤسسات في الاستطلاعات التي استند إليها التقرير أفادت باستخدام AI في وظيفة تنظيمية واحدة على الأقل خلال 2025، مقابل 78% في 2024. هذه بيانات استطلاعية وليست تعدادًا لكل المؤسسات.</div>', unsafe_allow_html=True)

    st.subheader("شكل 1 — لماذا انتشر AI؟")
    st.markdown("""
<div class="flow">
  <div class="node">البيانات<br>Data</div><div class="arrow">+</div>
  <div class="node">قوة الحوسبة<br>Computing</div><div class="arrow">+</div>
  <div class="node">الخوارزميات<br>Algorithms</div><div class="arrow">+</div>
  <div class="node">الإنترنت<br>Internet</div><div class="arrow">→</div>
  <div class="node">تطبيقات AI</div><div class="arrow">→</div>
  <div class="node">تحليل وقرار أفضل</div>
</div>
""", unsafe_allow_html=True)

    adoption = pd.DataFrame({
        "السنة": ["2024", "2025"],
        "نسبة المؤسسات التي أفادت باستخدام AI (%)": [78, 88]
    }).set_index("السنة")
    st.bar_chart(adoption, use_container_width=True)
    st.caption("المصدر: Stanford AI Index 2026. يعرض الرسم بيانات الاستطلاع كما وردت في التقرير.")

elif choice == sections[2]:
    st.subheader("2. ما هو الذكاء الاصطناعي؟")
    st.success(
        "تعريف تعليمي مبسط: الذكاء الاصطناعي هو مجال يهتم بأنظمة حاسوبية تستطيع "
        "معالجة المعلومات لتنفيذ مهام مثل التعلم، التنبؤ، التعرف على الأنماط، "
        "التوصية، فهم اللغة، إنتاج المحتوى أو دعم القرار."
    )
    st.write(
        "يعرض Russell & Norvig الذكاء الاصطناعي كمجال واسع يشمل الاستدلال والتعلم واللغة الطبيعية "
        "والرؤية الحاسوبية والروبوتات واتخاذ القرار. كما يركز تعريف OECD المحدّث لنظام AI على "
        "إنتاج مخرجات مثل التنبؤات والمحتوى والتوصيات أو القرارات انطلاقًا من المدخلات."
    )
    st.markdown("""
<div class="card-grid">
  <div class="card"><h4>🧠 يتعلم</h4><p>يستخلص أنماطًا من البيانات في بعض الأنظمة.</p></div>
  <div class="card"><h4>🔮 يتنبأ</h4><p>مثل توقع الطلب أو مخاطر التعثر.</p></div>
  <div class="card"><h4>💬 يفهم/يعالج اللغة</h4><p>تلخيص، ترجمة، محادثة، تحليل نص.</p></div>
  <div class="card"><h4>👁️ يتعرف</h4><p>تحليل الصور أو الصوت أو الأنماط.</p></div>
  <div class="card"><h4>✨ يولّد</h4><p>نصوصًا أو صورًا أو صوتًا.</p></div>
  <div class="card"><h4>🧭 يدعم القرار</h4><p>يقدم تنبؤًا أو توصية للمدير.</p></div>
</div>
""", unsafe_allow_html=True)

elif choice == sections[3]:
    st.subheader("3. ماذا يستطيع AI أن يفعل؟")
    st.markdown("""
<div class="flow">
  <div class="node">Learn<br>يتعلم</div>
  <div class="node">Predict<br>يتنبأ</div>
  <div class="node">Classify<br>يصنّف</div>
  <div class="node">Generate<br>يولّد</div>
  <div class="node">Recommend<br>يوصي</div>
</div>
""", unsafe_allow_html=True)
    st.markdown("""
| الوظيفة | سؤال بسيط | مثال إداري |
|---|---|---|
| **Prediction** التنبؤ | ماذا قد يحدث؟ | توقع المبيعات |
| **Classification** التصنيف | إلى أي فئة ينتمي؟ | عملية بنكية طبيعية/مشبوهة |
| **Recommendation** التوصية | ماذا نقترح؟ | منتج مناسب للعميل |
| **Generation** التوليد | هل يمكن إنتاج محتوى؟ | إنشاء نص أو صورة |
| **Recognition** التعرف | ماذا يوجد هنا؟ | كشف عيب في منتج |
| **Decision Support** دعم القرار | ما المعلومة التي يحتاجها المدير؟ | تقدير مخاطر الاستثمار |
""")

elif choice == sections[4]:
    st.subheader("4. هل كل برنامج حاسوبي AI؟")
    st.write("لا. هذه أمثلة تساعد على التمييز:")
    examples = [
        ("آلة حاسبة تحسب 25 × 35", "ليس AI لمجرد إجراء العملية الحسابية."),
        ("Excel يجمع المبيعات", "تحليل/حوسبة تقليدية، وليس بالضرورة AI."),
        ("نظام يتنبأ بمبيعات الشهر القادم من بيانات سابقة", "قد يستخدم Machine Learning."),
        ("ChatGPT يلخص تقريرًا", "تطبيق للذكاء الاصطناعي التوليدي."),
        ("نظام بنك يكتشف معاملات مشبوهة", "يمكن أن يستخدم AI/ML.")
    ]
    for title, explanation in examples:
        with st.expander(title):
            st.write(explanation)

    st.markdown('<div class="note"><b>قاعدة مهمة:</b> ليس كل تحليل بيانات ذكاءً اصطناعيًا، وليس كل أتمتة ذكاءً اصطناعيًا.</div>', unsafe_allow_html=True)

elif choice == sections[5]:
    st.subheader("5. الفرق بين النظام التقليدي ونظام AI")
    st.markdown("""
<div class="compare">
  <div class="box">
    <h3>⚙️ نظام تقليدي</h3>
    <ul>
      <li>ينفذ غالبًا قواعد وإجراءات محددة مسبقًا.</li>
      <li>مناسب للمهام الروتينية والواضحة.</li>
      <li>مثال: حساب الضريبة وفق معادلة ثابتة.</li>
    </ul>
  </div>
  <div class="box">
    <h3>🤖 نظام يستخدم AI</h3>
    <ul>
      <li>قد يستخدم الاستدلال أو التعلم أو التنبؤ.</li>
      <li>قد ينتج احتمالات أو توصيات.</li>
      <li>مثال: تقدير احتمال تعثر العميل.</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)
    st.warning(
        "التقسيم السابق تعليمي وليس حدًا مطلقًا. بعض أنظمة AI، مثل الأنظمة الخبيرة، "
        "تستخدم قواعد صريحة. لذلك التعلم من البيانات ليس شرطًا في كل نظام AI."
    )

    st.subheader("Automation أم Augmentation؟")
    st.markdown("""
<div class="compare">
  <div class="box">
    <h3>Automation — الأتمتة</h3>
    <p>الآلة تتولى تنفيذ مهمة أو جزء من مهمة كان الإنسان يؤديها.</p>
  </div>
  <div class="box">
    <h3>Augmentation — تعزيز القدرات</h3>
    <p>الإنسان وAI يعملان معًا لتحسين التحليل أو الأداء أو القرار.</p>
  </div>
</div>
""", unsafe_allow_html=True)

elif choice == sections[6]:
    st.subheader("6. أبرز تقنيات الذكاء الاصطناعي")
    st.markdown("""
<div class="flow">
  <div class="node">Artificial Intelligence<br>AI</div>
  <div class="arrow">→</div>
  <div class="node">Machine Learning<br>ML</div>
  <div class="arrow">→</div>
  <div class="node">Deep Learning<br>DL</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card-grid">
  <div class="card"><h4>Machine Learning (ML)</h4><p>استخلاص أنماط من البيانات للتنبؤ أو التصنيف.</p></div>
  <div class="card"><h4>Deep Learning (DL)</h4><p>فرع من ML يعتمد على شبكات عصبية عميقة.</p></div>
  <div class="card"><h4>NLP</h4><p>معالجة اللغة الطبيعية: نصوص، محادثة، ترجمة، تلخيص.</p></div>
  <div class="card"><h4>Computer Vision</h4><p>تحليل الصور والفيديو.</p></div>
  <div class="card"><h4>Generative AI</h4><p>إنتاج نصوص أو صور أو صوت أو محتوى جديد.</p></div>
  <div class="card"><h4>Expert Systems</h4><p>تمثيل خبرة وقواعد لاتخاذ استنتاجات في مجال محدد.</p></div>
</div>
""", unsafe_allow_html=True)

    st.caption("ملاحظة: الخريطة تبسيط تعليمي، وبعض المجالات تتداخل في الواقع.")

elif choice == sections[7]:
    st.subheader("7. الذكاء الاصطناعي في علوم التسيير")
    st.write("يمكن ربط AI مباشرة بوظائف المؤسسة:")
    st.markdown("""
| وظيفة المؤسسة | أمثلة على تطبيقات AI |
|---|---|
| **Marketing — التسويق** | تحليل سلوك العملاء، التوصيات، التخصيص |
| **Finance — المالية** | تقييم المخاطر، كشف الاحتيال، التنبؤ |
| **Human Resources — الموارد البشرية** | تحليل بيانات العاملين ودعم بعض القرارات |
| **Accounting — المحاسبة** | اكتشاف معاملات غير معتادة وأتمتة أعمال متكررة |
| **Operations — العمليات** | التنبؤ بالطلب، المخزون، الجدولة |
| **Management — الإدارة** | دعم القرار والتخطيط وتحليل السيناريوهات |
""")
    st.markdown("""
<div class="flow">
  <div class="node">بيانات المؤسسة</div><div class="arrow">→</div>
  <div class="node">AI / Analytics</div><div class="arrow">→</div>
  <div class="node">تنبؤ أو توصية</div><div class="arrow">→</div>
  <div class="node">قرار إداري</div>
</div>
""", unsafe_allow_html=True)

elif choice == sections[8]:
    st.subheader("8. AI وتحليل البيانات واتخاذ القرار")
    st.write("ليس كل تحليل بيانات AI. يمكن التفكير في الأسئلة الإدارية بالتدرج التالي:")
    st.markdown("""
<div class="flow">
  <div class="node">ماذا حدث؟<br>Descriptive</div><div class="arrow">→</div>
  <div class="node">لماذا حدث؟<br>Diagnostic</div><div class="arrow">→</div>
  <div class="node">ماذا قد يحدث؟<br>Predictive</div><div class="arrow">→</div>
  <div class="node">ماذا نفعل؟<br>Decision / Recommendation</div>
</div>
""", unsafe_allow_html=True)

    st.subheader("شكل — AI كأداة دعم قرار")
    st.markdown("""
<div class="flow">
  <div class="node">البيانات</div><div class="arrow">→</div>
  <div class="node">التحليل / النموذج</div><div class="arrow">→</div>
  <div class="node">Prediction / Recommendation</div><div class="arrow">→</div>
  <div class="node">المدير</div><div class="arrow">→</div>
  <div class="node">القرار</div>
</div>
""", unsafe_allow_html=True)

    st.info(
        "الفكرة الأساسية: AI يمكن أن يحسن المعلومات المتاحة للمدير، لكن القرار الإداري "
        "يحتاج أيضًا إلى السياق والخبرة والمسؤولية."
    )

elif choice == sections[9]:
    st.subheader("9. دراسة حالة: تسرب العملاء Customer Churn")
    st.write(
        "شركة تجزئة لديها 50,000 عميل. لاحظت أن جزءًا منهم يتوقف سنويًا عن الشراء."
    )
    st.subheader("البيانات المتاحة")
    st.markdown("""
- عدد المشتريات.
- قيمة المشتريات.
- مدة العلاقة مع العميل.
- عدد الشكاوى.
- الاستجابة للعروض.
- بيانات سلوكية أخرى إذا كانت قانونية ومناسبة للغرض.
""")
    st.markdown("""
<div class="flow">
  <div class="node">بيانات العملاء</div><div class="arrow">→</div>
  <div class="node">Machine Learning</div><div class="arrow">→</div>
  <div class="node">احتمال المغادرة</div><div class="arrow">→</div>
  <div class="node">المدير</div><div class="arrow">→</div>
  <div class="node">إجراء مناسب</div>
</div>
""", unsafe_allow_html=True)

    st.subheader("جرّب")
    q = st.multiselect(
        "ما الإجراءات الإدارية الممكنة بعد اكتشاف عميل معرض للمغادرة؟",
        ["تقديم عرض مناسب", "الاتصال بالعميل", "تحسين الخدمة", "حذف العميل تلقائيًا من النظام"]
    )
    if q:
        correct = {"تقديم عرض مناسب", "الاتصال بالعميل", "تحسين الخدمة"}
        if set(q).issubset(correct):
            st.success("اختيارات منطقية. لاحظ أن AI قدم تنبؤًا، بينما القرار والإجراء إداريان.")
        else:
            st.warning("حذف العميل تلقائيًا ليس نتيجة منطقية لمجرد ارتفاع احتمال المغادرة.")

elif choice == sections[10]:
    st.subheader("Quiz تفاعلي")
    questions = [
        ("أي عبارة أدق؟",
         ["كل برنامج حاسوبي هو AI", "AI هو ChatGPT فقط", "AI مجال يضم قدرات مثل التنبؤ والتعلم والتوصية", "AI يعني الروبوت فقط"],
         2),
        ("Machine Learning هو:", ["بديل عن AI", "جزء من AI", "نوع من قواعد البيانات", "برنامج محاسبة"], 1),
        ("Deep Learning هو:", ["أوسع من AI", "جزء من Machine Learning", "مرادف لـ Excel", "لا علاقة له بالبيانات"], 1),
        ("أي مثال يمثل Prediction؟", ["جمع المبيعات السابقة", "حفظ ملف", "توقع مبيعات الشهر القادم", "طباعة فاتورة"], 2),
        ("Automation وAI:", ["مترادفان دائمًا", "لا علاقة بينهما", "قد يتداخلان لكنهما ليسا المفهوم نفسه", "AI أقدم من الحاسوب"], 2),
    ]
    score = 0
    for i, (qtext, opts, correct) in enumerate(questions, start=1):
        ans = st.radio(f"{i}. {qtext}", opts, key=f"q{i}", index=None)
        if ans is not None and opts.index(ans) == correct:
            score += 1
    if st.button("إظهار النتيجة"):
        st.metric("النتيجة", f"{score} / {len(questions)}")
        if score == len(questions):
            st.success("ممتاز. فهمك للمفاهيم الأساسية واضح.")
        elif score >= 3:
            st.info("جيد. راجع فقط النقاط التي التبست عليك.")
        else:
            st.warning("يفضل مراجعة الأقسام الأساسية قبل الانتقال للمحاضرة الثانية.")

elif choice == sections[11]:
    st.subheader("نشاط TD رقم 1")
    st.write("يعمل الطلبة في مجموعات صغيرة. لكل حالة يجيبون عن ثلاثة أسئلة:")
    st.markdown("""
**ما البيانات؟ → ماذا يفعل AI؟ → ما القرار البشري؟**
""")
    st.markdown("""
| الحالة | مهمة المجموعة |
|---|---|
| برنامج يحسب راتب الموظف وفق قواعد ثابتة | AI أم أتمتة تقليدية؟ |
| متجر يقترح منتجات بناء على سلوك العميل | ما وظيفة AI؟ |
| بنك يتنبأ بتعثر العميل | ما البيانات الممكن استخدامها؟ |
| شركة تتوقع الطلب على المنتج | ما المخرج الذي ينتجه النموذج؟ |
| ChatGPT يلخص تقريرًا إداريًا | ما الفائدة؟ وما الخطر المحتمل؟ |
""")
    st.subheader("مهمة تمهيدية للمحاضرة الثانية")
    st.info("هل تعتقد أن الذكاء الاصطناعي بدأ مع ChatGPT؟ اكتب إجابة من 3–4 أسطر فقط مع سبب واحد.")

elif choice == sections[12]:
    st.subheader("المراجع الأساسية للمحاضرة")
    refs = [
        "Russell, S. J., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach (4th ed.). Pearson.",
        "OECD. (2024). Explanatory memorandum on the updated OECD definition of an AI system. OECD Artificial Intelligence Papers, No. 8.",
        "Raisch, S., & Krakowski, S. (2021). Artificial intelligence and management: The automation–augmentation paradox. Academy of Management Review, 46(1).",
        "Shrestha, Y. R., Ben-Menahem, S. M., & von Krogh, G. (2019). Organizational decision-making structures in the age of artificial intelligence. California Management Review, 61(4), 66–83.",
        "Stanford Institute for Human-Centered Artificial Intelligence. (2026). AI Index Report 2026.",
        "SDAIA. دليل الذكاء الاصطناعي للتنفيذيين. (مرجع داعم ضمن ملفات المقياس).",
        "أبو النصر، مدحت محمد. الذكاء الاصطناعي في المنظمات الذكية. (مرجع عربي داعم ضمن ملفات المقياس).",
    ]
    for ref in refs:
        st.write("• " + ref)

    st.divider()
    st.caption(
        "ملاحظة منهجية: المراجع الأكاديمية والمؤسسية هي أساس المفاهيم، "
        "أما المواد التعليمية العربية فتستخدم للتبسيط البيداغوجي ودعم الأمثلة."
    )
