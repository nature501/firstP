# 🚀 CLAUDE.md - Enhanced Project Template

> **Template Version**: 2.0 Enhanced  
> **Author**: Enhanced for practical Claude Code usage  
> **Last Updated**: 2025-09-23  
> **Project**: [PROJECT_NAME]  
> **Description**: [PROJECT_DESCRIPTION]

This file provides comprehensive guidance to Claude Code for working with code in this repository. It incorporates real-world best practices and addresses common pitfalls encountered by Claude Code users.

## 🚨 CRITICAL RULES - MANDATORY COMPLIANCE

> **⚠️ RULE ACKNOWLEDGMENT SYSTEM ⚠️**  
> **Claude Code MUST explicitly acknowledge these rules before starting ANY task**

### 📋 **MANDATORY PRE-TASK CHECKLIST**
Before ANY code execution, Claude Code must respond with:
```
✅ CRITICAL RULES ACKNOWLEDGED - I will follow all prohibitions and requirements
📋 PRE-TASK VERIFICATION COMPLETE:
  - Searched for existing implementations ✓
  - Verified no root directory file creation ✓  
  - Confirmed proper tool usage ✓
  - Task agents ready for long operations ✓
```

---

## ⛔ ABSOLUTE PROHIBITIONS

### 🚫 **FILE MANAGEMENT VIOLATIONS**
```yaml
NEVER_CREATE_IN_ROOT:
  # 絕不在根目錄建立檔案 - 破壞專案結構
  description: "Root directory files pollute project structure"
  correct_approach: "Use src/main/[language]/ structure"
  examples:
    wrong: "script.py in root"
    right: "src/main/python/script.py"

NEVER_DUPLICATE_FILES:
  # 絕不建立重複檔案 - 造成維護噩夢
  description: "Prevents technical debt and confusion"
  prohibited_patterns:
    - "*_v2.py, *_new.js, *_enhanced.py"
    - "manager_updated.py, utils_improved.js"
    - "handler_final.py, processor_latest.py"
  correct_approach: "Extend and refactor existing files"

NEVER_OUTPUT_TO_ROOT:
  # 絕不直接輸出到根目錄 - 污染工作空間
  description: "Maintains clean workspace organization"
  use_instead: "output/, results/, generated/, temp/"
```

### 🚫 **TOOL USAGE VIOLATIONS**
```yaml
NEVER_USE_DEPRECATED_COMMANDS:
  # 絕不使用已棄用的指令 - 會導致錯誤
  description: "These commands fail in Claude Code environment"
  prohibited: ["find", "grep", "cat", "head", "tail", "ls"]
  use_instead: ["Read", "LS", "Grep", "Glob", "Write", "Edit"]

NEVER_USE_INTERACTIVE_FLAGS:
  # 絕不使用互動模式 - Claude Code 不支援
  description: "Interactive modes not supported in Claude Code"
  prohibited: ["git -i", "npm -i", "pip -i"]
  use_instead: "Non-interactive equivalents with explicit parameters"

NEVER_HARDCODE_VALUES:
  # 絕不硬編碼數值 - 降低可維護性
  description: "Reduces maintainability and flexibility"
  examples:
    wrong: "API_URL = 'https://api.example.com'"
    right: "API_URL = os.getenv('API_URL', default_url)"
```

---

## ✅ MANDATORY REQUIREMENTS

### 📝 **VERSION CONTROL REQUIREMENTS**
```yaml
COMMIT_DISCIPLINE:
  # 提交紀律 - 確保進度不會丟失
  frequency: "After every completed task/feature"
  message_format: "feat/fix/docs: Brief description\n\nDetailed changes:\n- Change 1\n- Change 2"
  timing: "Never skip commits even for small changes"

GITHUB_BACKUP_PROTOCOL:
  # GitHub 備份協議 - 防止工作遺失
  command: "git push origin main"
  timing: "Immediately after every commit"
  verification: "Check push success before proceeding"
  failure_handling: "Retry with detailed error reporting"
```

### 🔧 **OPERATION REQUIREMENTS**
```yaml
TASK_AGENT_USAGE:
  # 任務代理使用 - 防止長時間操作中斷
  threshold: "Operations longer than 30 seconds"
  examples: ["File processing", "API calls", "Builds", "Tests"]
  reason: "Bash commands terminate on context switch"

TODOWRITE_FOR_COMPLEXITY:
  # 複雜任務分解 - 提高成功率和可追蹤性
  threshold: "Tasks with 3+ steps"
  benefits: ["Parallel execution", "Progress tracking", "Error isolation"]
  structure: "TodoWrite → Parallel agents → Git checkpoints → Validation"

READ_BEFORE_EDIT:
  # 編輯前必讀 - 避免編輯工具失敗
  description: "Edit/Write tools fail without prior file reading"
  workflow: "Read(file) → Understand structure → Edit/Write"
  exception: "New file creation only"
```

### 🔍 **TECHNICAL DEBT PREVENTION**
```yaml
SEARCH_FIRST_PRINCIPLE:
  # 搜尋優先原則 - 防止重複開發
  description: "Always search for existing implementations before creating new"
  tools: ["Grep", "Glob", "LS"]
  search_patterns:
    - "functionality.*keyword"
    - "class.*[ClassName]"
    - "def.*[function_name]"
  decision_tree: "Found existing? → Extend | Not found? → Create new"

SINGLE_SOURCE_OF_TRUTH:
  # 單一真實來源 - 防止邏輯分散
  description: "One authoritative implementation per concept"
  violations: ["Multiple managers", "Duplicate utilities", "Scattered logic"]
  solution: "Consolidate into single, well-designed module"

EXTEND_NOT_DUPLICATE:
  # 擴充不重複 - 保持程式碼整潔
  description: "Enhance existing functionality rather than duplicating"
  approach: "Read → Understand → Refactor → Extend"
  benefits: ["Better maintainability", "Consistent behavior", "Reduced complexity"]
```

---

## 🎯 SMART WORKFLOW PATTERNS

### 🧠 **COGNITIVE LOAD MANAGEMENT**
```yaml
CONTEXT_CHECKPOINT_SYSTEM:
  # 上下文檢查點系統 - 管理長時間會話
  description: "Prevent context overflow and maintain focus"
  triggers:
    - "Working > 1 hour continuously"
    - "Memory usage feels high"
    - "Responses becoming less accurate"
  actions:
    - "Use /compact command"
    - "Summary commit with detailed message"
    - "Consider session break"

INFORMATION_CHUNKING:
  # 資訊分塊 - 提高處理效率
  description: "Break complex information into digestible pieces"
  examples:
    - "Large files: Process in sections"
    - "Complex features: Implement incrementally"
    - "Multiple tasks: Prioritize and sequence"
```

### 🔄 **ERROR RECOVERY PATTERNS**
```yaml
GRACEFUL_FAILURE_HANDLING:
  # 優雅的失敗處理 - 從錯誤中學習和恢復
  description: "Handle failures systematically to prevent cascading issues"
  error_categories:
    syntax_errors: "Fix immediately, test thoroughly"
    logic_errors: "Debug step-by-step, add logging"
    tool_failures: "Try alternative approaches, report if persistent"
  recovery_protocol:
    1. "Acknowledge error clearly"
    2. "Analyze root cause"
    3. "Implement fix with explanation"
    4. "Add prevention measures"
    5. "Document learning"

DEBUGGING_METHODOLOGY:
  # 除錯方法論 - 系統化問題解決
  description: "Systematic approach to identifying and fixing issues"
  steps:
    1. "Reproduce issue reliably"
    2. "Isolate problem scope"
    3. "Form hypothesis"
    4. "Test hypothesis"
    5. "Implement solution"
    6. "Verify fix"
    7. "Document solution"
```

### 📊 **QUALITY ASSURANCE PATTERNS**
```yaml
PROGRESSIVE_VALIDATION:
  # 漸進式驗證 - 確保品質遞增
  description: "Validate functionality at each development stage"
  stages:
    unit_level: "Individual functions work correctly"
    integration_level: "Components work together"
    system_level: "Complete feature functions as expected"
    user_level: "Meets actual user requirements"

CODE_REVIEW_CHECKLIST:
  # 程式碼檢查清單 - 確保程式碼品質
  description: "Self-review checklist for code quality"
  checks:
    functionality: "Does it work as intended?"
    readability: "Is it easy to understand?"
    maintainability: "Is it easy to modify?"
    performance: "Does it perform adequately?"
    security: "Are there security considerations?"
    documentation: "Is it properly documented?"
```

---

## 🎨 PROJECT STRUCTURE TEMPLATES

### 📁 **ADAPTIVE PROJECT STRUCTURES**
```yaml
STRUCTURE_SELECTION_CRITERIA:
  # 結構選擇標準 - 根據專案需求選擇合適結構
  simple_project:
    criteria: "Single developer, < 10 files, basic functionality"
    structure: "src/, tests/, docs/, output/"
  
  standard_project:
    criteria: "Team project, modular design, multiple features"
    structure: "src/main/[lang]/{core,utils,models,services,api}/"
  
  enterprise_project:
    criteria: "Large team, complex architecture, multiple modules"
    structure: "Complete enterprise structure with all components"
  
  ai_ml_project:
    criteria: "Data science, ML models, experiments, MLOps"
    structure: "Includes data/, models/, notebooks/, experiments/"
```

### 🏗️ **ENHANCED STRUCTURE DEFINITIONS**
```yaml
# Simple Project (適合初學者和小型專案)
SIMPLE_STRUCTURE:
  directories:
    src/: "Source code - main application logic"
    tests/: "Test files - unit and integration tests"
    docs/: "Documentation - user guides and technical docs"
    output/: "Generated files - reports, exports, results"
    config/: "Configuration files - settings and parameters"
  
  files:
    "src/main.py": "Entry point for the application"
    "src/utils.py": "Utility functions and helpers"
    "tests/test_main.py": "Tests for main functionality"
    "config/settings.yaml": "Application configuration"
    "requirements.txt": "Python dependencies"

# Standard Project (適合中型應用程式)
STANDARD_STRUCTURE:
  directories:
    src/main/python/core/: "Core business logic"
    src/main/python/utils/: "Utility functions and helpers"
    src/main/python/models/: "Data models and entities"
    src/main/python/services/: "Business services and operations"
    src/main/python/api/: "API endpoints and controllers"
    src/main/resources/config/: "Configuration files"
    src/main/resources/assets/: "Static assets"
    src/test/unit/: "Unit tests"
    src/test/integration/: "Integration tests"
    docs/api/: "API documentation"
    tools/: "Development tools and scripts"

# AI/ML Project (適合機器學習專案)
AI_ML_STRUCTURE:
  directories:
    src/main/python/models/: "ML model definitions"
    src/main/python/training/: "Training scripts and pipelines"
    src/main/python/inference/: "Inference and prediction code"
    src/main/python/evaluation/: "Model evaluation metrics"
    data/raw/: "Original datasets"
    data/processed/: "Cleaned and transformed data"
    notebooks/exploratory/: "Data exploration notebooks"
    notebooks/experiments/: "ML experiments"
    models/trained/: "Trained model artifacts"
    experiments/configs/: "Experiment configurations"
    experiments/results/: "Experiment results and metrics"
```

---

## 🛠️ ADVANCED TOOL USAGE

### 🔧 **TOOL OPTIMIZATION PATTERNS**
```yaml
EFFICIENT_FILE_OPERATIONS:
  # 高效檔案操作 - 最佳化檔案處理流程
  description: "Optimize file operations for better performance"
  patterns:
    batch_operations: "Process multiple files in single operation"
    streaming: "Use streaming for large files"
    caching: "Cache frequently accessed data"
  
  examples:
    wrong: "Read each file separately in loop"
    right: "Use Glob to get file list, batch process"

SMART_SEARCH_STRATEGIES:
  # 智慧搜尋策略 - 提高搜尋效率和準確性
  description: "Advanced search patterns for finding existing code"
  strategies:
    broad_to_specific: "Start with general terms, narrow down"
    multi_pattern: "Use multiple search patterns to ensure coverage"
    cross_reference: "Verify results with different search approaches"
  
  search_patterns:
    functionality: "class.*Manager|function.*process|def.*handle"
    data_structures: "class.*Model|@dataclass|TypedDict"
    apis: "route|endpoint|@app|def.*api"
```

### 📋 **TASK MANAGEMENT STRATEGIES**
```yaml
PARALLEL_EXECUTION_PATTERNS:
  # 並行執行模式 - 最大化處理效率
  description: "Execute independent tasks simultaneously"
  suitable_for:
    - "File processing operations"
    - "Independent feature development"
    - "Data validation tasks"
    - "Test suite execution"
  
  implementation:
    1. "Identify independent tasks"
    2. "Launch Task agents for each"
    3. "Monitor progress"
    4. "Consolidate results"
    5. "Commit integrated solution"

DEPENDENCY_MANAGEMENT:
  # 依賴關係管理 - 確保任務執行順序正確
  description: "Handle task dependencies systematically"
  types:
    sequential: "Task B requires Task A completion"
    conditional: "Task C depends on Task A result"
    parallel_with_sync: "Tasks run parallel but sync at points"
  
  tools:
    TodoWrite: "For dependency mapping"
    Task_agents: "For parallel execution"
    Git_checkpoints: "For progress tracking"
```

---

## 🚨 COMMON PITFALLS AND SOLUTIONS

### ⚠️ **CRITICAL MISTAKE PATTERNS**
```yaml
CONTEXT_OVERFLOW_SYMPTOMS:
  # 上下文溢出症狀 - 識別和預防會話問題
  description: "Recognize when context is becoming overloaded"
  symptoms:
    - "Responses becoming generic or repetitive"
    - "Forgetting earlier conversation details"
    - "Making mistakes on previously established patterns"
    - "Suggesting solutions already tried"
  
  prevention:
    - "Use /compact regularly"
    - "Commit progress frequently"
    - "Document decisions in comments"
    - "Break complex tasks into sessions"

TECHNICAL_DEBT_ACCUMULATION:
  # 技術債務累積 - 識別和防止程式碼品質下降
  description: "Prevent technical debt before it becomes problem"
  warning_signs:
    - "Multiple files with similar names"
    - "Copy-pasted code blocks"
    - "Inconsistent naming conventions"
    - "Growing file sizes without refactoring"
  
  prevention_strategies:
    early_refactoring: "Refactor as soon as patterns emerge"
    naming_discipline: "Consistent, descriptive names"
    single_responsibility: "One clear purpose per file/function"
    regular_cleanup: "Periodic code review and cleanup"

TOOL_MISUSE_PATTERNS:
  # 工具誤用模式 - 避免常見的工具使用錯誤
  description: "Common tool usage mistakes and corrections"
  mistakes:
    using_bash_for_long_operations: "Use Task agents instead"
    not_reading_before_editing: "Always Read before Edit"
    hardcoding_file_paths: "Use relative paths and configuration"
    ignoring_error_messages: "Always address errors immediately"
```

### 🔧 **SOLUTION TEMPLATES**
```yaml
RAPID_RECOVERY_PROCEDURES:
  # 快速恢復程序 - 從常見問題中快速恢復
  description: "Quick procedures for common issues"
  scenarios:
    file_corruption:
      1. "Check git history: git log --oneline"
      2. "Restore from last good commit: git checkout HEAD~1 -- filename"
      3. "Review changes and re-apply carefully"
    
    context_confusion:
      1. "Use /compact to reduce context"
      2. "Summarize current state in comments"
      3. "Create checkpoint commit"
      4. "Continue with fresh focus"
    
    tool_failure:
      1. "Try alternative tool (Read vs Grep)"
      2. "Check file permissions and existence"
      3. "Use absolute paths if needed"
      4. "Report persistent issues for debugging"

ESCALATION_PROCEDURES:
  # 升級程序 - 處理複雜問題的系統化方法
  description: "When standard approaches don't work"
  levels:
    level_1: "Try alternative tools or approaches"
    level_2: "Break problem into smaller pieces"
    level_3: "Document issue and seek clarification"
    level_4: "Consider session restart with problem summary"
```

---

## 📈 PERFORMANCE OPTIMIZATION

### ⚡ **EFFICIENCY PATTERNS**
```yaml
RESOURCE_OPTIMIZATION:
  # 資源最佳化 - 提高處理效率
  description: "Optimize resource usage for better performance"
  strategies:
    memory_management:
      - "Process large files in chunks"
      - "Use generators for large datasets"
      - "Clear variables when no longer needed"
    
    time_optimization:
      - "Cache frequently accessed data"
      - "Use parallel processing for independent tasks"
      - "Optimize database queries and file I/O"
    
    context_optimization:
      - "Use /compact when context gets large"
      - "Summarize long conversations"
      - "Focus on current task relevance"

SCALABILITY_CONSIDERATIONS:
  # 可擴展性考量 - 設計可成長的系統
  description: "Design for future growth and complexity"
  principles:
    modular_design: "Components can be independently modified"
    loose_coupling: "Minimize dependencies between modules"
    configuration_driven: "Use config files for customization"
    documentation: "Clear documentation for future developers"
```

### 📊 **MONITORING AND METRICS**
```yaml
PROGRESS_TRACKING:
  # 進度追蹤 - 監控開發進度和品質
  description: "Track development progress and quality metrics"
  metrics:
    code_quality:
      - "Number of files in proper structure"
      - "Consistency of naming conventions"
      - "Test coverage percentage"
    
    productivity:
      - "Tasks completed per session"
      - "Time to complete similar tasks"
      - "Number of bugs introduced"
    
    maintenance:
      - "Frequency of refactoring needs"
      - "Time to understand existing code"
      - "Ease of adding new features"

QUALITY_GATES:
  # 品質關卡 - 確保品質標準
  description: "Quality checkpoints throughout development"
  checkpoints:
    before_commit:
      - "All tests pass"
      - "No syntax errors"
      - "Code follows project conventions"
    
    before_push:
      - "Integration tests pass"
      - "Documentation updated"
      - "No sensitive data included"
    
    milestone_review:
      - "Architecture review"
      - "Performance assessment"
      - "Security review"
```

---

## 🎯 CUSTOMIZATION GUIDELINES

### 🔧 **TEMPLATE ADAPTATION**
```yaml
PROJECT_SPECIFIC_CUSTOMIZATION:
  # 專案特定客製化 - 根據專案需求調整範本
  description: "Adapt this template to your specific project needs"
  customization_points:
    project_structure:
      consider: "Team size, complexity, technology stack"
      action: "Choose appropriate structure template"
    
    naming_conventions:
      consider: "Team preferences, industry standards"
      action: "Establish and document conventions"
    
    workflow_patterns:
      consider: "Development methodology, team practices"
      action: "Adapt workflow to match team needs"

RULE_EVOLUTION:
  # 規則演進 - 持續改進和調整規則
  description: "Continuously improve rules based on experience"
  evolution_triggers:
    - "Repeated violations of current rules"
    - "Discovery of new best practices"
    - "Changes in team structure or technology"
    - "Feedback from development experience"
  
  evolution_process:
    1. "Identify improvement opportunity"
    2. "Analyze current rule effectiveness"
    3. "Propose rule modification"
    4. "Test new rule in practice"
    5. "Update template with learnings"
```

### 📝 **DOCUMENTATION MAINTENANCE**
```yaml
TEMPLATE_MAINTENANCE:
  # 範本維護 - 保持範本的實用性和準確性
  description: "Keep template current and useful"
  maintenance_schedule:
    weekly: "Review rule violations and effectiveness"
    monthly: "Update based on new learnings"
    quarterly: "Major review and restructuring if needed"
  
  maintenance_checklist:
    - "Are rules preventing actual problems?"
    - "Are new problems emerging that need rules?"
    - "Is the template easy to understand and follow?"
    - "Are examples current and relevant?"

KNOWLEDGE_TRANSFER:
  # 知識轉移 - 確保團隊成員理解和遵循規則
  description: "Ensure team understands and follows template"
  strategies:
    onboarding: "New team members review template thoroughly"
    training: "Regular sessions on template usage"
    examples: "Maintain examples of good and bad practices"
    feedback: "Regular feedback on template effectiveness"
```

---

## 🎪 ADVANCED PATTERNS

### 🧩 **ARCHITECTURAL PATTERNS**
```yaml
MICROSERVICE_PREPARATION:
  # 微服務準備 - 為未來的微服務架構做準備
  description: "Structure code for potential microservice architecture"
  principles:
    service_boundaries: "Clear boundaries between different domains"
    data_isolation: "Each service manages its own data"
    api_contracts: "Well-defined interfaces between services"
    independent_deployment: "Services can be deployed independently"

PLUGIN_ARCHITECTURE:
  # 外掛程式架構 - 設計可擴展的系統
  description: "Design for extensibility through plugins"
  components:
    core_system: "Base functionality that remains stable"
    plugin_interface: "Standard interface for extensions"
    plugin_registry: "Mechanism to discover and load plugins"
    configuration: "Settings to control plugin behavior"
```

### 🔄 **INTEGRATION PATTERNS**
```yaml
API_INTEGRATION_STANDARDS:
  # API 整合標準 - 標準化外部系統整合
  description: "Standardize how external systems are integrated"
  standards:
    authentication: "Consistent auth handling across integrations"
    error_handling: "Standard error response processing"
    retry_logic: "Exponential backoff for failed requests"
    monitoring: "Logging and metrics for all API calls"

DATA_PIPELINE_PATTERNS:
  # 資料管道模式 - 標準化資料處理流程
  description: "Standardize data processing workflows"
  stages:
    ingestion: "Collecting data from various sources"
    validation: "Ensuring data quality and consistency"
    transformation: "Converting data to required format"
    storage: "Persisting processed data"
    monitoring: "Tracking pipeline health and performance"
```

---

## 📚 LEARNING AND IMPROVEMENT

### 🎓 **CONTINUOUS LEARNING**
```yaml
SKILL_DEVELOPMENT:
  # 技能發展 - 持續提升開發能力
  description: "Continuously improve development skills"
  areas:
    technical_skills:
      - "Learn new programming languages and frameworks"
      - "Understand design patterns and architectural principles"
      - "Stay updated with industry best practices"
    
    soft_skills:
      - "Improve problem-solving approaches"
      - "Enhance communication and documentation"
      - "Develop project management capabilities"

KNOWLEDGE_SHARING:
  # 知識分享 - 促進團隊學習和成長
  description: "Share learnings and best practices"
  methods:
    documentation: "Document solutions and lessons learned"
    code_reviews: "Share knowledge through code reviews"
    presentations: "Regular tech talks on interesting topics"
    mentoring: "Help junior developers learn and grow"
```

### 🔍 **REFLECTION AND ADAPTATION**
```yaml
RETROSPECTIVE_PRACTICES:
  # 回顧實踐 - 定期檢討和改進
  description: "Regular reflection on development practices"
  frequency: "Weekly team retrospectives, monthly process review"
  questions:
    - "What worked well this week/month?"
    - "What could be improved?"
    - "What new challenges emerged?"
    - "How can we adapt our processes?"

FEEDBACK_INTEGRATION:
  # 回饋整合 - 將回饋轉化為改進
  description: "Systematically integrate feedback into improvements"
  sources:
    - "User feedback on delivered features"
    - "Team feedback on development process"
    - "Performance metrics and monitoring data"
    - "External code reviews and audits"
  
  integration_process:
    1. "Collect feedback systematically"
    2. "Analyze patterns and themes"
    3. "Prioritize improvement opportunities"
    4. "Implement changes incrementally"
    5. "Measure impact of changes"
```

---

## 🏁 CONCLUSION

This enhanced template provides a comprehensive framework for effective Claude Code usage. It addresses real-world challenges and provides practical solutions for common development scenarios.

### 🎯 **KEY TAKEAWAYS**
1. **Prevention over correction**: Focus on preventing problems rather than fixing them
2. **Systematic approach**: Use structured workflows and checklists
3. **Continuous improvement**: Regularly adapt and improve practices
4. **Knowledge sharing**: Document and share learnings with the team

### 🚀 **NEXT STEPS**
1. Customize this template for your specific project needs
2. Establish team agreements on rule adherence
3. Set up monitoring and feedback mechanisms
4. Plan regular template reviews and updates

---

**Remember**: This template is a living document. Adapt it based on your experience and needs. The goal is to create a productive, maintainable, and enjoyable development environment.