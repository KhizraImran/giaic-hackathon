import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title" style={{fontFamily: "'Cormorant Garamond', Georgia, serif", color: "#5a4a42"}}>
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle" style={{color: "#7d6e65", fontFamily: "'Nunito', 'Open Sans', sans-serif"}}>
          {siteConfig.tagline}
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--primary button--lg"
            to="/docs/introduction">
            Explore the Textbook
          </Link>
          <Link
            className={`button button--outline button--secondary button--lg ${styles.secondaryButton}`}
            to="/docs/module1_ros2">
            Start Learning
          </Link>
        </div>
      </div>
    </header>
  );
}

function FeatureCard({ title, description, icon }: { title: string; description: string; icon: string }) {
  return (
    <div className={styles.featureCard}>
      <div style={{ fontSize: '2.5rem', marginBottom: '1rem', textAlign: 'center' }}>{icon}</div>
      <Heading as="h3">{title}</Heading>
      <p>{description}</p>
    </div>
  );
}

function CallToAction() {
  return (
    <section className={styles.callToAction}>
      <div className="container">
        <Heading as="h2">Begin Your Journey in Physical AI</Heading>
        <p>Dive into the fascinating world where artificial intelligence meets the physical world. Master the technologies that will shape the future of robotics and human-machine interaction.</p>
        <div className={styles.buttons}>
          <Link
            className="button button--primary button--lg"
            to="/docs/introduction">
            Start Reading
          </Link>
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();

  const features = [
    {
      title: 'ROS 2 Fundamentals',
      description: 'Master the Robot Operating System that connects every component of modern robotics, from sensors to actuators.',
      icon: '🤖',
    },
    {
      title: 'Digital Twins',
      description: 'Simulate and test robotic behaviors in virtual environments before deploying to real hardware with Gazebo and Unity.',
      icon: '🔄',
    },
    {
      title: 'AI-Powered Control',
      description: 'Learn how NVIDIA Isaac brings advanced perception and decision-making to humanoid robots.',
      icon: '🧠',
    },
    {
      title: 'Vision-Language-Action',
      description: 'Integrate LLMs with robotics to create systems that understand natural language and execute complex tasks.',
      icon: '💬',
    },
    {
      title: 'Humanoid Robotics',
      description: 'Design and control bipedal robots capable of natural human-like interactions and movements.',
      icon: '🦾',
    },
    {
      title: 'Conversational AI',
      description: 'Build robots that can understand and respond to human speech for intuitive human-robot interaction.',
      icon: '🗣️',
    },
  ];

  return (
    <Layout
      title={`Physical AI & Humanoid Robotics Textbook`}
      description="Comprehensive textbook for learning Physical AI and Humanoid Robotics">
      <HomepageHeader />
      <main>
        <section className={styles.featuredSection}>
          <div className="container">
            <Heading as="h2">What You'll Learn</Heading>
            <div className={styles.featuresGrid}>
              {features.map((feature, index) => (
                <FeatureCard
                  key={index}
                  title={feature.title}
                  description={feature.description}
                  icon={feature.icon}
                />
              ))}
            </div>
          </div>
        </section>

        <CallToAction />
      </main>
    </Layout>
  );
}
