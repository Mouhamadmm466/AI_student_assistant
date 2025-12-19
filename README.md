# AI-Student-Assitant - Academic Learning Platform

<div align="center">

![StudyGenius](public/images/logo.png)

**A modern, intelligent learning companion designed to help students master complex subjects effortlessly.**

[View Live Demo](https://mm-ai-study-assistant.vercel.app/) • [Report Bug](https://github.com/Mouhamadmm466/v0-ai-study-assistant-frontend/issues) • [Request Feature](https://github.com/Mouhamadmm466/v0-ai-study-assistant-frontend/issues)

[![Deployed on Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=for-the-badge&logo=vercel)](https://mm-ai-study-assistant.vercel.app/)
[![Next.js](https://img.shields.io/badge/Next.js-16.0-black?style=for-the-badge&logo=next.js)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19.2-61DAFB?style=for-the-badge&logo=react)](https://react.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.1-38B2AC?style=for-the-badge&logo=tailwind-css)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Dark Mode](#dark-mode)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

StudyGenius is a modern, responsive learning platform built to streamline academic study workflows. The application provides students and educators with powerful tools to enhance learning efficiency through interactive features, intuitive design, and seamless integration with learning backends.

**Live Application:** [https://mm-ai-study-assistant.vercel.app/](https://mm-ai-study-assistant.vercel.app/)

---

## ✨ Features

### 📝 Note Summarization
- **Smart Content Processing** - Transform lengthy study notes into concise, actionable summaries
- **Flexible Detail Levels** - Choose between concise, detailed, or bullet-point formats
- **Copy-Paste Ready** - Large textarea interface for easy content input

### ❓ Practice Question Generation
- **Quiz Builder** - Generate customizable practice questions from any study material
- **Multiple Question Types** - Support for multiple-choice, short-answer, and true/false questions
- **Difficulty Control** - Select from easy, medium, and hard difficulty levels
- **Interactive Quiz Mode** - Navigate through questions with hidden answers and type indicators

### 💡 Concept Explanation
- **In-Depth Learning** - Get comprehensive explanations of academic concepts
- **Contextual Understanding** - Optional context input for personalized explanations
- **Professional Formatting** - Well-structured explanations with clear typography

### 🎨 Modern User Interface
- **Clean & Minimalist Design** - Focus on content with thoughtful whitespace
- **Responsive Layout** - Seamlessly adapts from mobile devices to large displays
- **Dark Mode Support** - Eye-friendly dark theme with persistent user preference
- **Smooth Interactions** - Loading states, error handling, and success notifications

### 🌓 Dark Mode
- Toggle between light and dark themes
- Automatically persists user preference in browser storage
- Carefully selected color palette to reduce eye strain

---

## 🛠 Tech Stack

### Frontend
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Next.js** | 16.0+ | React framework with SSR and static generation |
| **React** | 19.2+ | UI library with hooks and functional components |
| **TypeScript** | 5.0+ | Type safety and improved development experience |
| **Tailwind CSS** | 4.1+ | Utility-first CSS framework for responsive design |
| **Radix UI** | Latest | Accessible component primitives |
| **React Hook Form** | 7.60+ | Efficient form state management |
| **Zod** | 3.25+ | TypeScript-first schema validation |
| **Lucide React** | 0.454+ | Modern icon library |
| **Sonner** | 1.7+ | Toast notifications |
| **Next Themes** | 0.4+ | Dark mode implementation |

### Backend Integration
- **FastAPI** - Python-based REST API
- **Base URL:**----

### Deployment
- **Platform:** Vercel
- **CI/CD:** GitHub integration with automatic deployments

---

## 🚀 Getting Started

### Prerequisites
- Node.js 18.0 or higher
- npm, yarn, or pnpm package manager
- Git

### Installation

1. **Clone the repository**
   \`\`\`bash
   git clone https://github.com/Mouhamadmm466/v0-ai-study-assistant-frontend.git
   cd v0-ai-study-assistant-frontend
   \`\`\`

2. **Install dependencies**
   \`\`\`bash
   npm install

   yarn install
   
   pnpm install
   \`\`\`

4. **Set up environment variables**
   Create a `.env.local` file in the root directory:
   \`\`\`env

5. **Start the development server**
   \`\`\`bash
   npm run dev
   # or
   yarn dev
   # or
   pnpm dev
   \`\`\`

6. **Open in browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

---

## 📖 Usage

### Landing Page
- Browse features and benefits of AI-Student-Assitant
- View real-world use cases and learning statistics
- Click "Get Started" to access the main application

### Summarize Notes
1. Navigate to the **"Summarize Notes"** tab
2. Paste your study material in the textarea
3. Select desired detail level (concise, detailed, or bullet-points)
4. Click **"Generate Summary"**
5. Review results in the output area

### Generate Practice Questions
1. Navigate to the **"Generate Questions"** tab
2. Enter your study content
3. Set the number of questions (1-20)
4. Select difficulty level
5. Choose question types (multiple-choice, short-answer, true/false)
6. Click **"Create Practice Quiz"**
7. Navigate through questions and toggle answers

### Explain Concepts
1. Navigate to the **"Explain Concepts"** tab
2. Enter the concept you want to understand
3. Optionally provide relevant context or notes
4. Click **"Get Explanation"**
5. Read the comprehensive explanation

### Theme Toggle
- Click the sun/moon icon in the top-right corner
- Switch between light and dark modes
- Preference is automatically saved

---

## 🔌 API Integration

### Endpoints

#### 1. Summarize Notes
\`\`\`
POST /api/summarize
\`\`\`

**Request Body:**
\`\`\`json
{
  "content": "Your study notes here...",
  "detail": "concise" | "detailed" | "bullet-points"
}
\`\`\`

**Response:**
\`\`\`json
{
  "summary": "Summarized content..."
}
\`\`\`

#### 2. Generate Questions
\`\`\`
POST /api/questions
\`\`\`

**Request Body:**
\`\`\`json
{
  "content": "Study material...",
  "count": 5,
  "difficulty": "easy" | "medium" | "hard",
  "types": {
    "mc": true,
    "short": false,
    "tf": false
  }
}
\`\`\`

**Response:**
\`\`\`json
{
  "questions": [
    {
      "question": "Question text?",
      "answer": "Answer text",
      "type": "mc" | "short" | "tf"
    }
  ]
}
\`\`\`

#### 3. Explain Concepts
\`\`\`
POST /api/explain
\`\`\`

**Request Body:**
\`\`\`json
{
  "query": "Concept to explain",
  "context": "Optional context..." | ""
}
\`\`\`

**Response:**
\`\`\`json
{
  "explanation": "Detailed explanation..."
}
\`\`\`

---

## 🌓 Dark Mode

Dark mode is built-in and uses `next-themes` for seamless theme management:

- **Toggle Location:** Top-right corner of the header
- **Storage:** Browser localStorage (persists across sessions)
- **Default Theme:** Light mode
- **Colors:** Carefully selected palette to reduce eye strain in dark environments

---

## 📦 Project Structure

\`\`\`
v0-ai-study-assistant-frontend/
├── app/
│   ├── layout.tsx           # Root layout with theme provider
│   ├── page.tsx             # Landing page + main app
│   ├── globals.css          # Global styles and theme tokens
│   └── favicon.ico          # Application favicon
├── public/
│   └── images/              # Asset images
│       ├── logo.png         # StudyGenius logo
│       ├── hero-ai.png      # Hero section image
│       ├── feature-reading.png
│       └── student-study.png
├── components/
│   └── theme-provider.tsx   # Dark mode provider component
├── lib/
│   └── utils.ts             # Utility functions
├── package.json             # Dependencies and scripts
├── tailwind.config.js       # Tailwind CSS configuration
├── tsconfig.json            # TypeScript configuration
└── README.md                # This file
\`\`\`

---

## 🎨 Design System

### Color Palette
- **Primary:** Soft teal/blue (oklch-based for accessibility)
- **Neutral:** Off-white to dark grey spectrum
- **Accent:** Complementary teal highlights

### Typography
- **Headings:** Clean, modern sans-serif (Geist font family)
- **Body:** Readable, accessible font sizes (14px minimum)
- **Line Height:** 1.4-1.6 for optimal readability

### Responsive Breakpoints
- **Mobile:** < 640px (single column)
- **Tablet:** 640px - 1024px (optimized layout)
- **Desktop:** > 1024px (multi-column, full features)

---

## 🚀 Deployment

### Deploy to Vercel (Recommended)

1. **Push to GitHub**
   \`\`\`bash
   git push origin main
   \`\`\`

2. **Connect to Vercel**
   - Visit [vercel.com](https://vercel.com)
   - Click "New Project" and select this repository
   - Vercel auto-detects Next.js configuration

3. **Deploy**
   - Click "Deploy"
   - Your application will be live in seconds
   - Automatic deployments on every push to `main`

### Environment Variables
- Environment variables required for production

### Custom Domain
- Configure custom domain in Vercel project settings
- DNS records will be provided for configuration

---

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. **Fork the repository**
   \`\`\`bash
   git clone https://github.com/Mouhamadmm466/mm-ai-study-assistant-frontend
   \`\`\`

2. **Create a feature branch**
   \`\`\`bash
   git checkout -b feature/Feature
   \`\`\`

3. **Commit changes**
   \`\`\`bash
   git commit -m 'Add some Feature'
   \`\`\`

4. **Push to branch**
   \`\`\`bash
   git push origin feature/Feature
   \`\`\`

5. **Open a Pull Request**

### Code Standards
- Follow existing code style
- Use TypeScript for type safety
- Test responsive design on mobile and desktop

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

- 📧 **Email:** [Support](mailto:mouhamadmm@icloud.com)
- 🐛 **Report Issues:** [GitHub Issues](https://github.com/Mouhamadmm466/v0-ai-study-assistant-frontend/issues)
- 💬 **Discussions:** [GitHub Discussions](https://github.com/Mouhamadmm466/v0-ai-study-assistant-frontend/discussions)

---

## 🙏 Acknowledgments

- UI Components from [Radix UI](https://radix-ui.com/)
- Icons from [Lucide React](https://lucide.dev/)
-  Deployed on [Vercel](https://vercel.com)

---

<div align="center">

**Made for students, by Mouhamad Mamane

[⬆ back to top](#studygenius---academic-learning-platform)

</div>
