import streamlit as st
import yfinance as yf

st.title("Stock Price Viewer")

ticker = st.text_input("Enter a stock ticker")

period = st.selectbox(
    "Choose a time period",
    ["1mo", "3mo", "6mo", "1y", "5y"])

if ticker:
    stock = yf.Ticker(ticker)

    data = stock.history(period=period)

    if data.empty:
        st.write("Stock not found")
    else:
        st.write("Stock:", ticker.upper())
        st.line_chart(data["Close"])
        
