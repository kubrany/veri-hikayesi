# %% [markdown]
# # Üniversite kapısında kadınlar erkekleri ne zaman geçti?
# Veri: Dünya Bankası, brüt yükseköğretim okullaşma oranı (SE.TER.ENRR.FE ve .MA). Çalıştırma: bu klasörden "Restart & Run All".
# %% [markdown]
# ## 1. Veri yükleme
# %%
import pandas as pd, glob
def load(code):
    f = glob.glob(f'../data/raw/API_{code}_*.csv')[0]
    d = pd.read_csv(f, skiprows=4)
    yrs = [c for c in d.columns if c.isdigit()]
    return d.melt(id_vars=['Country Name','Country Code'], value_vars=yrs, var_name='year', value_name=code)
fe, ma = load('SE.TER.ENRR.FE'), load('SE.TER.ENRR.MA')
df = fe.merge(ma, on=['Country Name','Country Code','year'])
df.columns = ['name','code','year','female','male']
meta = pd.read_csv(glob.glob('../data/raw/Metadata_Country_*.csv')[0])[['Country Code','Region']]
meta.columns = ['code','region']
df = df.merge(meta, on='code')
print('Ham satır:', len(df))
# %% [markdown]
# ## 2. Temizleme
# Kararlar: (a) Bölge bilgisi boş olanlar ülke değil "dünya, gelir grubu" gibi toplamlardır, çıkarıldı. (b) Kadın veya erkek değeri eksik satırlar çıkarıldı, çünkü karşılaştırma yapılamaz. (c) Erkek oranı 0 olan satırlar çıkarıldı.
# %%
df = df[df.region.notna()]
df = df.dropna(subset=['female','male']); df = df[df.male > 0]
df['year'] = df.year.astype(int)
df['name'] = df.name.str.replace(',', ';'); df['region'] = df.region.str.replace(',', ';')
print('Temiz satır:', len(df), '| ülke:', df.code.nunique(), '| yıllar:', df.year.min(), '-', df.year.max())
# %% [markdown]
# ## 3. Keşifsel analiz
# %%
df['women_more'] = df.female > df.male
share = df.groupby('year').women_more.mean().mul(100).round(1)
n = df.groupby('year').size()
print(share[n >= 50].iloc[::5])
tur = df[df.code == 'TUR'].sort_values('year')
print(tur[['year','female','male']].tail(12))
# %% [markdown]
# ## 4. Sitede kullanılan özet dosyanın dışa aktarımı
# %%
import os
os.makedirs('../site/data', exist_ok=True); os.makedirs('../data/processed', exist_ok=True)
out = df[['code','name','region','year','female','male']].round(2)
out.to_csv('../site/data/gap.csv', index=False); out.to_csv('../data/processed/gap.csv', index=False)
print('Yazıldı:', len(out), 'satır')
