import React from 'react';
import Layout from '@theme-original/Layout';
import Chatbot from '../../components/Chatbot';

export default function LayoutWrapper(props) {
  return (
    <>
      <Layout {...props}>
        {props.children}
      </Layout>
      <Chatbot />
    </>
  );
}
