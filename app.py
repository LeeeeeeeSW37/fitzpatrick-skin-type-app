import streamlit as st

st.set_page_config(page_title="Fitzpatrick 피부 타입 테스트", page_icon=":sun_with_face:")

st.title("Fitzpatrick 피부 타입 테스트")

score_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

questions = [
    ("햇볕에 노출되었을 때 보통 어떤 반응을 하나요?", [
        "A: 쉽게 타고 벗겨진다",
        "B: 조금 타고 약간 벗겨진다",
        "C: 드물게 탄다",
        "D: 거의 안 탄다"
    ]),
    ("햇볕에 노출되면 피부가 잘 태닝되나요?", [
        "A: 전혀 안 된다",
        "B: 약간 된다",
        "C: 쉽게 된다",
        "D: 아주 잘 된다"
    ]),
    ("자연적인 피부색은 어떤가요?", [
        "A: 아주 희고 밝은 피부",
        "B: 밝은 피부",
        "C: 중간 피부",
        "D: 어두운 피부"
    ]),
    ("머리카락 색은 어떤가요?", [
        "A: 빨강 또는 금발",
        "B: 밝은 갈색",
        "C: 갈색",
        "D: 검정"
    ]),
    ("눈 색깔은 어떤가요?", [
        "A: 파랑/녹색",
        "B: 회색/헤이즐",
        "C: 갈색",
        "D: 짙은 갈색/검정"
    ])
]

answers = []

with st.form("skin_type_form"):
    for i, (q, options) in enumerate(questions):
        choice = st.selectbox(f"{i+1}. {q}", options, key=i)
        answers.append(choice[0])
    submitted = st.form_submit_button("피부 타입 확인")

def classify_fitzpatrick(answers):
    total_score = sum([score_map[a] for a in answers])
    if total_score <= 7:
        return "Type I: 매우 밝고 쉽게 타며 태닝되지 않음"
    elif total_score <= 10:
        return "Type II: 밝은 피부, 쉽게 타고 약간 태닝됨"
    elif total_score <= 13:
        return "Type III: 보통 피부, 때때로 타고 점차 태닝됨"
    elif total_score <= 16:
        return "Type IV: 중간~올리브 톤, 드물게 타고 잘 태닝됨"
    elif total_score <= 19:
        return "Type V: 어두운 피부, 거의 타지 않고 매우 잘 태닝됨"
    else:
        return "Type VI: 아주 어두운 피부, 절대 타지 않고 태닝 잘 됨"

if submitted:
    result = classify_fitzpatrick(answers)
    st.success(f"당신의 Fitzpatrick 피부 타입은: **{result}**")
