import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


st.title('米の食味試験　分散分析')

from PIL import Image

uploaded_file = st.file_uploader("Upload file", type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    
    st.subheader("")
    st.write("精白米外観　分散分析")
    #(1)精白米外観　分散分析
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    ols_lm = smf.ols(formula='精白米外観 ~ 品種', data=df).fit()
    anova_result = sm.stats.anova_lm(ols_lm, typ=2)
    st.dataframe(anova_result)
    st.write("精白米外観　Tukey-Kramerの多重検定")
    #(1)精白米外観　Tukey-Kramerの多重検定
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    tukey_result_jan = pairwise_tukeyhsd(df.loc[:, '精白米外観'].values, df.loc[:, '品種'].values)
    st.text(tukey_result_jan)
    
    st.subheader("")
    st.write("外観　分散分析")
    #(2)外観　分散分析
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    ols_lm = smf.ols(formula='外観 ~ 品種', data=df).fit()
    anova_result = sm.stats.anova_lm(ols_lm, typ=2)
    st.dataframe(anova_result)
    st.write("外観　Tukey-Kramerの多重検定")
    #(2)外観　Tukey-Kramerの多重検定
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    tukey_result_jan = pairwise_tukeyhsd(df.loc[:, '外観'].values, df.loc[:, '品種'].values)
    st.text(tukey_result_jan)    
    
    st.subheader("")
    st.write("香り　分散分析")
    #(3)香り　分散分析
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    ols_lm = smf.ols(formula='香り ~ 品種', data=df).fit()
    anova_result = sm.stats.anova_lm(ols_lm, typ=2)
    st.dataframe(anova_result)
    st.write("香り　Tukey-Kramerの多重検定")
    #(3)香り　Tukey-Kramerの多重検定
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    tukey_result_jan = pairwise_tukeyhsd(df.loc[:, '香り'].values, df.loc[:, '品種'].values)
    st.text(tukey_result_jan)    
    
    st.subheader("")
    st.write("硬さ　分散分析")
    #(4)硬さ　分散分析
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    ols_lm = smf.ols(formula='硬さ ~ 品種', data=df).fit()
    anova_result = sm.stats.anova_lm(ols_lm, typ=2)
    st.dataframe(anova_result)
    st.write("硬さ　Tukey-Kramerの多重検定")
    #(4)硬さ　Tukey-Kramerの多重検定
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    tukey_result_jan = pairwise_tukeyhsd(df.loc[:, '硬さ'].values, df.loc[:, '品種'].values)
    st.text(tukey_result_jan)   
    
    st.subheader("")
    st.write("粘り　分散分析")
    #(5)粘り　分散分析
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    ols_lm = smf.ols(formula='粘り ~ 品種', data=df).fit()
    anova_result = sm.stats.anova_lm(ols_lm, typ=2)
    st.dataframe(anova_result)
    st.write("粘り　Tukey-Kramerの多重検定")
    #(5)粘り　Tukey-Kramerの多重検定
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    tukey_result_jan = pairwise_tukeyhsd(df.loc[:, '粘り'].values, df.loc[:, '品種'].values)
    st.text(tukey_result_jan)   
    
    st.subheader("")
    st.write("総合評価　分散分析")
    #(6)総合評価　分散分析
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    ols_lm = smf.ols(formula='総合評価 ~ 品種', data=df).fit()
    anova_result = sm.stats.anova_lm(ols_lm, typ=2)
    st.dataframe(anova_result)
    st.write("総合評価　Tukey-Kramerの多重検定")
    #(6)総合評価　Tukey-Kramerの多重検定
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    tukey_result_jan = pairwise_tukeyhsd(df.loc[:, '総合評価'].values, df.loc[:, '品種'].values)
    st.text(tukey_result_jan)    