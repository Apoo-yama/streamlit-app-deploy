import streamlit as st
# 「title()」メソッドでタイトルを表示
st.title("サンプルアプリ②: 少し複雑なWebアプリ")
# 「write()」メソッドによるテキスト出力を4連続で行っています。
st.write("##### 動作モード1: 文字数カウント")  #テキストに「#」を付けると見出しテキストとして大きく太く表示されます。
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("##### 動作モード2: BMI値の計算")
st.write("身長と体重を入力することで、肥満度を表す体型指数のBMI値を算出できます。")

# 「radio()」メソッドを使い、ラジオボタンを表示しています。
selected_item = st.radio(
    "動作モードを選択してください。",
    ["文字数カウント", "BMI値の計算"]
)

# 続いて、「divider()」メソッドを使って区切り線を表示しています。
st.divider()

# 次に、ラジオボタンでどちらを選択したかによって表示パーツを分岐させている以下のコードです。
if selected_item == "文字数カウント":
    input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")
    text_count = len(input_message)
#「BMI値の計算」が選択された場合、「text_input()」を使って、身長と体重を受け取る入力フォームを表示しています。
else:
    height = st.text_input(label="身長（cm）を入力してください。")
    weight = st.text_input(label="体重（kg）を入力してください。")

# 最後に、「button()」メソッドで「実行」ボタンを表示し、ボタンがクリックされたときの処理をif文で記述しています。
if st.button("実行"): # ボタンがクリックされたときの処理
    st.divider() # 区切り線を表示

#「文字数カウント」が選択されている場合、入力フォームに値が入っていたら先ほどカウントした文字数を表示
    if selected_item == "文字数カウント":
        if input_message:
            st.write(f"文字数: **{text_count}**")
# 入力フォームが空の状態でボタンが押された場合はエラーメッセージを「error()」メソッドを使って以下のように表示しています。
        else:
            st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")

# 「BMI値の計算」が選択されている場合、身長と体重の両方が入力されていたらBMI値を計算して表示
    else:
        if height and weight:
            try:
                bmi = round(int(weight) / ((int(height)/100) ** 2), 1)
                st.write(f"BMI値: {bmi}")
# 身長と体重のどちらかに数値以外の文字が入力されていた場合、計算時にエラーになるため、例外処理で対応しています。
            except ValueError as e:
                st.error("身長と体重は数値で入力してください。")
# 身長と体重のフォームに値が入力されていない場合、「error()」メソッドでエラーメッセージが表示されます。
        else:
            st.error("身長と体重をどちらも入力してください。")