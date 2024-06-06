import logging

logger = logging.getLogger(__name__)

def preprocess_data(df):
    try:
        logger.info("Preprocessing data")
        df.fillna('', inplace=True)
        df['combined_features'] =  df['Title'] + ' '+ df['Author'] + ' ' + df['Genre'] + ' ' + df['Publisher']
        
        # Create a new column for genre-specific combined features
        df['genre_combined_features'] = df.apply(lambda x: x['Title'] + ' ' + x['Author'] + ' ' + x['Publisher'] if x['Genre'] != '' else '', axis=1)
        
        return df
    except Exception as e:
        logger.error("Error during data preprocessing: %s", e)
        raise
