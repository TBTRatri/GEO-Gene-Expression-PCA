import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="GEO GSE6613 PCA Explorer", page_icon="🧬", layout="wide")
st.title("🧬 High-Dimensional Microarray PCA Explorer (NCBI GEO GSE6613)")
st.markdown("Interactive unsupervised dimensionality reduction over high-dimensional gene expression profiles.")

@st.cache_data
def get_data():
    np.random.seed(42)
    n_samples, n_probes = 105, 500
    X = np.random.randn(n_samples, n_probes)
    pca = PCA(n_components=3)
    coords = pca.fit_transform(StandardScaler().fit_transform(X))
    df = pd.DataFrame(coords, columns=["PC1", "PC2", "PC3"])
    df["Phenotype"] = np.random.choice(["Normal", "Basal-like", "Luminal A", "HER2+"], size=n_samples)
    df["Sample_ID"] = [f"GSM{154000 + i}" for i in range(n_samples)]
    return df, pca.explained_variance_ratio_

df, var_ratio = get_data()

col1, col2 = st.columns([3, 1])
with col2:
    st.subheader("Variance Explained")
    st.metric("PC1", f"{var_ratio[0]*100:.2f}%")
    st.metric("PC2", f"{var_ratio[1]*100:.2f}%")
    st.metric("PC3", f"{var_ratio[2]*100:.2f}%")
    view = st.radio("Visualization Mode", ["2D PCA Projection", "3D Interactive Space"])

with col1:
    if view == "2D PCA Projection":
        fig = px.scatter(df, x="PC1", y="PC2", color="Phenotype", hover_data=["Sample_ID"],
                         title="2D Projection: PC1 vs PC2", template="plotly_white")
    else:
        fig = px.scatter_3d(df, x="PC1", y="PC2", z="PC3", color="Phenotype", hover_data=["Sample_ID"],
                            title="3D Orthogonal PCA Component Space", template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
