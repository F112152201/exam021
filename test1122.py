import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import sqlite3

# 初始化資料庫
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        payment INTEGER DEFAULT 0
    )
''')
conn.commit()

# 資料視覺化函數定義
def plot_gdp_data(df):
    df.columns = ['Year', 'Amount', 'Growth rate']
    df['Amount'] = df['Amount'].apply(lambda x: str(x).replace(',', '')).astype(float) / 1e6
    df['Year'] = df['Year'].astype(str).str.strip()
    years = df['Year']
    amounts = df['Amount']
    growth_rates = df['Growth rate']
    fig, ax1 = plt.subplots(figsize=(12, 6))
    bars = ax1.bar(years, amounts, color='blue', label='Amount (Million)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Amount (Million)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax2 = ax1.twinx()
    line, = ax2.plot(years, growth_rates, color='red', marker='o', label='Growth rate')
    ax2.set_ylabel('Growth rate (%)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.15))
    plt.title('GDP')
    st.pyplot(fig)

def plot_personal_economic_indicators(df):
    df.columns = ['Year', 'Personal GNI', 'Personal GDP', 'Personal NI', 'Personal expenditures']
    df['Personal GNI'] = df['Personal GNI'].apply(lambda x: str(x).replace(',', '')).astype(float) / 1e6
    df['Personal GDP'] = df['Personal GDP'].apply(lambda x: str(x).replace(',', '')).astype(float) / 1e6
    df['Personal NI'] = df['Personal NI'].apply(lambda x: str(x).replace(',', '')).astype(float) / 1e6
    df['Personal expenditures'] = df['Personal expenditures'].apply(lambda x: str(x).replace(',', '')).astype(float) / 1e6
    df['Year'] = df['Year'].astype(str).str.strip()
    years = df['Year']
    personal_gni = df['Personal GNI']
    personal_gdp = df['Personal GDP']
    personal_ni = df['Personal NI']
    personal_expenditures = df['Personal expenditures']
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(years, personal_gni, marker='o', label='Personal GNI (Million)', color='blue')
    ax1.plot(years, personal_gdp, marker='o', label='Personal GDP (Million)', color='orange')
    ax1.plot(years, personal_ni, marker='o', label='Personal NI (Million)', color='green')
    ax1.plot(years, personal_expenditures, marker='o', label='Personal expenditures (Million)', color='red')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Amount (Million)')
    ax1.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
    plt.title('Personal Economic Indicators')
    st.pyplot(fig)

def plot_earning_comparison(df):
    df.columns = ['Year', 'Economic growth rate(%)', 'National earning', 'Personal earning']
    df['National earning'] = df['National earning'].apply(lambda x: str(x).replace(',', '')).astype(float) / 1e6
    df['Personal earning'] = df['Personal earning'].apply(lambda x: str(x).replace(',', '')).astype(float) / 1e6
    df['Year'] = df['Year'].astype(str).str.strip()
    years = df['Year']
    national_earning = df['National earning']
    personal_earning = df['Personal earning']
    growth_rate = df['Economic growth rate(%)']
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(years, national_earning, marker='o', label='National earning (Million)', color='blue')
    ax1.plot(years, personal_earning, marker='o', label='Personal earning (Million)', color='orange')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Earnings (Million)')
    ax2 = ax1.twinx()
    ax2.plot(years, growth_rate, marker='o', label='Economic growth rate(%)', color='red')
    ax2.set_ylabel('Growth rate (%)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.85))
    plt.title('National vs Personal Earnings')
    st.pyplot(fig)

def plot_gni_comparison(df):
    df.columns = ['Year', 'Economic growth rate(%)', 'National GNI', 'Personal GNI']
    df['National GNI'] = df['National GNI'].apply(lambda x: str(x).replace(',', '')).astype(float) / 1e6
    df['Personal GNI'] = df['Personal GNI'].apply(lambda x: str(x).replace(',', '')).astype(float) / 1e6
    df['Year'] = df['Year'].astype(str).str.strip()
    years = df['Year']
    national_gni = df['National GNI']
    personal_gni = df['Personal GNI']
    growth_rate = df['Economic growth rate(%)']
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(years, national_gni, marker='o', label='National GNI (Million)', color='blue')
    ax1.plot(years, personal_gni, marker='o', label='Personal GNI (Million)', color='orange')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('GNI (Million)')
    ax2 = ax1.twinx()
    ax2.plot(years, growth_rate, marker='o', label='Economic growth rate(%)', color='red')
    ax2.set_ylabel('Growth rate (%)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.85))
    plt.title('National vs Personal GNI')
    st.pyplot(fig)

def plot_gdp_comparison(df):
    df.columns = ['Year', 'Economic growth rate', 'Domestic GDP', 'Personal GDP']
    df['Domestic GDP'] = df['Domestic GDP'].apply(lambda x: str(x).replace(',', '')).astype(float) / 1e6
    df['Personal GDP'] = df['Personal GDP'].apply(lambda x: str(x).replace(',', '')).astype(float) / 1e6
    df['Year'] = df['Year'].astype(str).str.strip()
    years = df['Year']
    domestic_gdp = df['Domestic GDP']
    personal_gdp = df['Personal GDP']
    growth_rate = df['Economic growth rate']
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(years, domestic_gdp, marker='o', label='Domestic GDP (Million)', color='blue')
    ax1.plot(years, personal_gdp, marker='o', label='Personal GDP (Million)', color='orange')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('GDP (Million)')
    ax2 = ax1.twinx()
    ax2.plot(years, growth_rate, marker='o', label='Economic growth rate(%)', color='red')
    ax2.set_ylabel('Growth rate (%)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.85))
    plt.title('National GDP vs Personal GDP')
    st.pyplot(fig)

# 主程式
def main():
    st.title("JimeeFirstWebApp")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['guest_chart_views'] = 0
        st.session_state['payment'] = False

    if st.session_state['logged_in']:
        st.write(f"歡迎，{st.session_state['username']}！")
        st.subheader("您已登入，感謝使用本應用！")

        # 匯入自訂 CSV 檔案功能
        uploaded_file = st.file_uploader("選擇要匯入的 CSV 檔案", type=["csv"])
        if uploaded_file is not None:
            try:
                df_custom = pd.read_csv(uploaded_file, header=0, encoding='latin1')  # 嘗試用latin1編碼
                st.write("以下是匯入的自訂 CSV 檔案資料：")
                st.write(df_custom.head())

                # 檢測 CSV 檔案並選擇合適的圖表類型
                if 'Year' in df_custom.columns:
                    if 'Amount' in df_custom.columns and 'Growth rate' in df_custom.columns:
                        plot_gdp_data(df_custom)
                    elif 'Personal GNI' in df_custom.columns and 'Personal GDP' in df_custom.columns and 'Personal NI' in df_custom.columns and 'Personal expenditures' in df_custom.columns:
                        plot_personal_economic_indicators(df_custom)
                    elif 'National earning' in df_custom.columns and 'Personal earning' in df_custom.columns:
                        plot_earning_comparison(df_custom)
                    elif 'National GNI' in df_custom.columns and 'Personal GNI' in df_custom.columns:
                        plot_gni_comparison(df_custom)
                    elif 'Domestic GDP' in df_custom.columns and 'Personal GDP' in df_custom.columns:
                        plot_gdp_comparison(df_custom)
                    else:
                        st.error("無法識別的 CSV 檔案結構。")
                else:
                    st.error("CSV 檔案中缺少 'Year' 欄位。")

            except Exception as e:
                st.error(f"匯入檔案時發生錯誤：{e}")

        if st.button("登出"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ""
            st.session_state['chart_views'] = 0
            st.session_state['payment'] = False
            st.experimental_rerun()

    else:
        menu = ["登入", "註冊"]
        choice = st.sidebar.selectbox("選擇操作", menu)

        if choice == "登入":
            login()
        elif choice == "註冊":
            signup()

        st.write("您目前以訪客身分查看此應用。請登入以查看圖表。")

def login():
    st.subheader("請登入")
    
    username = st.text_input("用戶名")
    password = st.text_input("密碼", type="password")

    if st.button("登入"):
        user = validate_login(username, password)
        if user:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['payment'] = False
            st.success("登入成功！")
            st.experimental_rerun()
        else:
            st.error("用戶名或密碼錯誤。")

def signup():
    st.subheader("註冊新帳戶")
    
    new_username = st.text_input("新用戶名")
    new_password = st.text_input("新密碼", type="password")

    if st.button("註冊"):
        if not validate_signup(new_username):
            create_user(new_username, new_password)
            st.success("註冊成功，請登入！")
        else:
            st.error("用戶名已存在，請選擇其他用戶名。")

def validate_login(username, password):
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return c.fetchone()

def validate_signup(username):
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    return c.fetchone()

def create_user(username, password):
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

def show_payment_page():
    st.subheader("付費繼續使用")
    st.write("請選擇您的付費方案：")
    plans = ["1個月 - NT$100", "3個月 - NT$250", "1年 - NT$900"]
    plan = st.selectbox("選擇方案", plans)
    if st.button("付款"):
        st.success(f"已成功購買 {plan} 方案！")
        st.session_state['chart_views'] = 0  # 重置查看次數
        st.session_state['payment'] = True
        st.session_state['show_payment_page'] = False
        st.experimental_rerun()

if __name__ == "__main__":
    if 'show_payment_page' in st.session_state and st.session_state['show_payment_page']:
        show_payment_page()
    else:
        main()

