import React, { useState, useEffect } from 'react';
import styles from './Chatbot.module.css';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

function Chatbot() {
  const { siteConfig } = useDocusaurusContext();
  const chatbotBackendUrl = siteConfig.customFields.chatbotBackendUrl;

  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [selectedText, setSelectedText] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const [isMinimized, setIsMinimized] = useState(false);

  useEffect(() => {
    const handleMouseUp = () => {
      const selection = window.getSelection();
      if (selection) {
        const text = selection.toString().trim();
        if (text.length > 0) {
          setSelectedText(text);
        }
      }
    };

    document.addEventListener('mouseup', handleMouseUp);

    return () => {
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, []);

  const handleQueryChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!query.trim()) {
      setError('Please enter a question.');
      return;
    }

    setLoading(true);
    setError('');
    setResponse('');

    try {
      const res = await fetch(`${chatbotBackendUrl}/rag/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_query: query,
          collection_name: 'book_content',
          selected_text: selectedText,
        }),
      });

      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.detail || 'Failed to fetch response from chatbot backend.');
      }

      const data = await res.json();
      setResponse(data.response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const toggleChat = () => {
    setIsOpen(!isOpen);
    if (!isOpen) {
      setIsMinimized(false);
    }
  };

  const minimizeChat = () => {
    setIsMinimized(!isMinimized);
  };

  if (!isOpen) {
    return (
      <button className={styles.chatbotToggle} onClick={toggleChat}>
        💬
      </button>
    );
  }

  if (isMinimized) {
    return (
      <div className={styles.chatbotWidgetMinimized}>
        <button className={styles.chatbotMinimizeToggle} onClick={minimizeChat}>
          💬 Textbook AI
        </button>
        <button className={styles.chatbotClose} onClick={toggleChat}>
          ×
        </button>
      </div>
    );
  }

  return (
    <div className={styles.chatbotWidget}>
      <div className={styles.chatbotHeader}>
        <h4>🤖 Textbook AI Assistant</h4>
        <div className={styles.chatbotHeaderButtons}>
          <button className={styles.chatbotMinimize} onClick={minimizeChat}>
            −
          </button>
          <button className={styles.chatbotClose} onClick={toggleChat}>
            ×
          </button>
        </div>
      </div>

      {selectedText && (
        <div className={styles.selectedTextIndicator}>
          <strong>Context:</strong> "{selectedText}"
        </div>
      )}

      <div className={styles.chatMessages}>
        {response && (
          <div className={styles.responseMessage}>
            <div className={styles.responseContent}>{response}</div>
          </div>
        )}
      </div>

      {error && <p className={styles.errorMessage}>{error}</p>}

      <form onSubmit={handleSubmit} className={styles.chatInputForm}>
        <input
          type="text"
          value={query}
          onChange={handleQueryChange}
          placeholder="Ask about the textbook..."
          className={styles.chatInput}
          disabled={loading}
        />
        <button type="submit" className={styles.chatSubmitButton} disabled={loading}>
          {loading ? (
            <span className={styles.loadingSpinner}></span>
          ) : (
            '➤'
          )}
        </button>
      </form>
    </div>
  );
}

export default Chatbot;
