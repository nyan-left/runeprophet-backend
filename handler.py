import os
os.environ[ 'MPLCONFIGDIR' ] = '/tmp/'
try:
  if os.environ.get("AWS_EXECUTION_ENV") is not None:
    import unzip_requirements
  import pandas as pd
  from fbprophet import Prophet
  import json
except(Exception):
  pass

def predict(event, context):
  try:
    data = json.loads(event['body'])
    df = pd.DataFrame(data)
    df.head()
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=30)
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    jsonResponse = forecast.to_json(orient='records', date_format='iso')
    print('Trying to return a response')
    print(jsonResponse[0:30])
    response = {
        "statusCode": 200,
        "body": jsonResponse
    }
    return response
  except Exception:
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
