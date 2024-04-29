import pandas as pd 
import category_encoders as ce 



data = {'color' :['red','green','yellow','green','yellow','red','green','yellow','green','yellow']}

df = pd.DataFrame(data) #convert dictionary to data frame..
print(df.head()) #show only first five record..

encoder = ce.BinaryEncoder(cols = ['color'])
#conver dimension based on binary digits

df_binary_encoder=encoder.fit_transform(df)
print(df_binary_encoder)
