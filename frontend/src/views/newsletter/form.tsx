import React, { FC, useState, ChangeEvent, FormEvent } from 'react';
import { Form, FormGroup, Input, Button, Label } from 'reactstrap';
import { apiPaths } from '../../constants';

const emailListRegex = /^[\w+.-]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,}(?:,\s*[\w+.-]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,})*$/;

interface NewsletterFormProps {
  newsletterId: number;
}

const NewsletterForm: FC<NewsletterFormProps> = ({ newsletterId }) => {
  const [file, setFile] = useState<File | null>(null);
  const [recipients, setRecipients] = useState('');
  const [sendToSubscribers, setSendToSubscribers] = useState(true);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    setFile(selectedFile || null);
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const isValid = emailListRegex.test(recipients);;
    if (!isValid) {
      alert('Invalid email list');
      return;
    }
  
    const formData = new FormData();

    if (file) formData.append('attachment', file as any);
  
    formData.append('recipients', recipients);
    formData.append('newsletter_id', newsletterId.toString());
    formData.append('send_to_subscribers', sendToSubscribers.toString());

    try {
      const response = await fetch(apiPaths.newsletters.send, {
        method: 'POST',
        body: formData,
      });
      console.log(response);
      if (response.ok) {
        // File successfully uploaded.
        console.log('File uploaded successfully.');
      } else {
        // Handle error response.
        console.error('Failed to upload file.');
      }
    } catch (error) {
      console.error('An error occurred:', error);
    }
  };

  return (
    <>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label htmlFor="recipients">Recipients</Label>
          <Input
            type="text"
            name="recipients"
            onChange={(e) => setRecipients(e.target.value)}
            placeholder="Enter a comma separated list of emails"
            value={recipients}
            required
          />
        </FormGroup>
        <FormGroup>
          <Label htmlFor="attachment">Attachment</Label>
          <Input type="file" name="attachment" accept=".png,.pdf" onChange={handleFileChange} />
        </FormGroup>
        <FormGroup check>
          <Input type="checkbox" checked={sendToSubscribers} onChange={(e) => setSendToSubscribers(e.target.checked)}/>
          {' '}
          <Label check>
            Check to also sent to the current subscribers
          </Label>
        </FormGroup>
        <Button type="submit" color="primary">Send Newsletter</Button>
      </Form>
    </>
  );
};

export default NewsletterForm;
