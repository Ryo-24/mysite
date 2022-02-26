import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit入門')

# st.write('DataFrame')
st.write('Display Image')

'start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    bar.progress(i+1)
    latest_iteration.text(f'Iteraiton: {i+1}')
    time.sleep(0.1)

'done!!'


left_colum, right_colum = st.columns(2)
button = left_colum.button('右カラムを表示')
if button:
    right_colum.write('ここは右カラムです．')

expander1 = st.expander('問い合わせ')
expander1.write('回答1')
expander2 = st.expander('問い合わせ')
expander2.write('回答2')

# condition = st.sidebar.slider('あなたの今の調子は',0 ,100, 50, 10)
# text = st.sidebar.text_input('あなたの趣味を教えてください．')

# 'condition:', condition
# 'あなたの趣味：', text


options =  st.selectbox(
    'あなたが好きな数字を教えてください．',
    list(range(1, 11))
)
'あなたが好きな数字は，' ,options, 'です．'

if st.checkbox('show image'):
    img = Image.open(r'C:\Users\ryohei\Desktop\python\web_app\Nissy.jpg')
    st.image(img, caption='Nissy',use_column_width=True)

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4, 5],
#     '2列目': [10, 20, 30, 40, 50]
# })

# st.dataframe(df, width=200, height=200)
# st.table(df)

"""
# 章
# 節
# 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.dataframe(df)

# st.line_chart(df)


df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)