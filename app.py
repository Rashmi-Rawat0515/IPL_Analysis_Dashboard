import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load data ──────────────────────────────────────────────
st.set_page_config(page_title="IPL Dashboard", layout="wide")

@st.cache_data
def load_data():
    matches = pd.read_csv("matches.csv")
    return matches

matches = load_data()

# ── Title ──────────────────────────────────────────────────
st.title("IPL Match Analysis Dashboard")
st.markdown("Exploring IPL data from 2008 to 2020")

# ── Sidebar filter ─────────────────────────────────────────
st.sidebar.header("Filter Data")
seasons = sorted(matches['season'].unique())
selected_season = st.sidebar.selectbox("Select Season", ["All"] + list(seasons))

if selected_season != "All":
    data = matches[matches['season'] == selected_season]
else:
    data = matches

# ── Metric cards ───────────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("Total Matches", len(data))
col2.metric("Total Seasons", data['season'].nunique())
col3.metric("Cities Covered", data['city'].nunique())

st.divider()

# ── Chart 1: Top teams by wins ─────────────────────────────
st.subheader("Top 10 Teams by Wins")
top_teams = data['winner'].value_counts().head(10)
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.barplot(x=top_teams.values, y=top_teams.index, palette="Blues_r", ax=ax1)
ax1.set_xlabel("Wins")
ax1.set_ylabel("Team")
st.pyplot(fig1)

st.divider()

# ── Chart 2: Matches per season ────────────────────────────
st.subheader("Matches Played Per Season")
season_counts = matches['season'].value_counts().sort_index()
fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.lineplot(x=season_counts.index, y=season_counts.values, marker="o", color="coral", ax=ax2)
ax2.set_xlabel("Season")
ax2.set_ylabel("Matches")
st.pyplot(fig2)

st.divider()

# ── Chart 3: Top host cities ───────────────────────────────
st.subheader("Top 10 Host Cities")
top_cities = data['city'].value_counts().head(10)
fig3, ax3 = plt.subplots(figsize=(10, 4))
sns.barplot(x=top_cities.values, y=top_cities.index, palette="Greens_r", ax=ax3)
ax3.set_xlabel("Matches Hosted")
ax3.set_ylabel("City")
st.pyplot(fig3)

st.divider()

# ── Chart 4: Top Player of the Match ──────────────────────
st.subheader("Top 10 Player of the Match Winners")
top_players = data['player_of_match'].value_counts().head(10)
fig4, ax4 = plt.subplots(figsize=(10, 4))
sns.barplot(x=top_players.values, y=top_players.index, palette="Oranges_r", ax=ax4)
ax4.set_xlabel("Awards")
ax4.set_ylabel("Player")
st.pyplot(fig4)