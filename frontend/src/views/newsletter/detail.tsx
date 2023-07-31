import React, { FC, useState } from 'react';
import { NewsletterProps } from '../../interfaces';
import NewsletterForm from './form';

interface NewsletterDetailProps {
  newsletter: NewsletterProps;
}

const NewsletterDetail: FC<NewsletterDetailProps> = ({ newsletter }) => {
  const { name, id } = newsletter;

  
  return (
    <div style={{ marginTop: 50 }}>
      <h1>{name}</h1>
      <NewsletterForm newsletterId={id} />
    </div>
  );
};

export default NewsletterDetail;
