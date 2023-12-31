import React, { FC, useEffect, useState } from 'react';
import { Table } from 'reactstrap';
import { apiPaths } from '../../constants';
import { NewsletterProps } from '../../interfaces';
import NewsletterDetail from './detail';


const Newsletter: FC = () => {
  const [newsletters, setNewsletters] = useState<NewsletterProps[]>([]);
  const [selectedNewsletter, setSelectedNewsletter] = useState<NewsletterProps>();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(apiPaths.newsletters.list);
        const jsonData = await response.json();
        setNewsletters(jsonData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  }, []);

  return (
    <>
      <h1>Newsletters</h1>
      <p>Click over a Newsletter row to start</p>
      {newsletters && (
        <Table hover>
          <thead>
            <tr>
              <th>Id</th>
              <th>Name</th>
              <th>Template</th>
            </tr>
          </thead>
          <tbody>
            {newsletters.map(({ id, name, subscribers, email_template }: NewsletterProps) => (
              <tr
                key={id}
                onClick={() => setSelectedNewsletter({ id: id, name: name, subscribers: subscribers, email_template })}
                style={{ cursor: 'pointer' }}
              >
                <td>{id}</td>
                <td>{name}</td>
                <td>{email_template}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      )}
      {selectedNewsletter && <NewsletterDetail newsletter={selectedNewsletter} />}
    </>
  );
};

export default Newsletter;
