<?php
/**
 * 旅遊諮詢表單小工具
 *
 * @package NatureTour
 * @version 1.0.0
 */

if (!defined('ABSPATH')) {
    exit;
}

class Travel_Inquiry_Form_Widget extends \Elementor\Widget_Base {

    public function get_name() {
        return 'travel_inquiry_form';
    }

    public function get_title() {
        return esc_html__('旅遊諮詢表單', 'naturetour');
    }

    public function get_icon() {
        return 'eicon-form-horizontal';
    }

    public function get_categories() {
        return ['naturetour'];
    }

    public function get_keywords() {
        return ['travel', 'inquiry', 'form', 'contact', '旅遊', '諮詢', '表單'];
    }

    protected function register_controls() {

        // 內容設定
        $this->start_controls_section(
            'content_section',
            [
                'label' => esc_html__('表單設定', 'naturetour'),
                'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
            ]
        );

        $this->add_control(
            'form_title',
            [
                'label' => esc_html__('表單標題', 'naturetour'),
                'type' => \Elementor\Controls_Manager::TEXT,
                'default' => esc_html__('開始規劃您的夢想旅程', 'naturetour'),
                'placeholder' => esc_html__('輸入表單標題...', 'naturetour'),
            ]
        );

        $this->add_control(
            'form_description',
            [
                'label' => esc_html__('表單描述', 'naturetour'),
                'type' => \Elementor\Controls_Manager::TEXTAREA,
                'default' => esc_html__('填寫下方表單，我們的專業旅遊顧問將在24小時內與您聯繫', 'naturetour'),
                'placeholder' => esc_html__('輸入表單描述...', 'naturetour'),
            ]
        );

        $this->add_control(
            'enable_multi_step',
            [
                'label' => esc_html__('啟用多步驟表單', 'naturetour'),
                'type' => \Elementor\Controls_Manager::SWITCHER,
                'label_on' => esc_html__('是', 'naturetour'),
                'label_off' => esc_html__('否', 'naturetour'),
                'return_value' => 'yes',
                'default' => 'yes',
            ]
        );

        $this->add_control(
            'form_style',
            [
                'label' => esc_html__('表單樣式', 'naturetour'),
                'type' => \Elementor\Controls_Manager::SELECT,
                'default' => 'modern',
                'options' => [
                    'classic' => esc_html__('經典', 'naturetour'),
                    'modern' => esc_html__('現代', 'naturetour'),
                    'minimal' => esc_html__('簡約', 'naturetour'),
                ],
            ]
        );

        $this->end_controls_section();

        // 樣式設定
        $this->start_controls_section(
            'style_section',
            [
                'label' => esc_html__('樣式設定', 'naturetour'),
                'tab' => \Elementor\Controls_Manager::TAB_STYLE,
            ]
        );

        $this->add_control(
            'form_background_color',
            [
                'label' => esc_html__('背景顏色', 'naturetour'),
                'type' => \Elementor\Controls_Manager::COLOR,
                'scheme' => [
                    'type' => \Elementor\Core\Schemes\Color::get_type(),
                    'value' => \Elementor\Core\Schemes\Color::COLOR_1,
                ],
                'selectors' => [
                    '{{WRAPPER}} .travel-inquiry-form' => 'background-color: {{VALUE}}',
                ],
                'default' => '#FFFFFF',
            ]
        );

        $this->add_group_control(
            \Elementor\Group_Control_Typography::get_type(),
            [
                'name' => 'title_typography',
                'label' => esc_html__('標題字體', 'naturetour'),
                'scheme' => \Elementor\Core\Schemes\Typography::TYPOGRAPHY_1,
                'selector' => '{{WRAPPER}} .form-title',
            ]
        );

        $this->add_control(
            'button_background_color',
            [
                'label' => esc_html__('按鈕顏色', 'naturetour'),
                'type' => \Elementor\Controls_Manager::COLOR,
                'selectors' => [
                    '{{WRAPPER}} .inquiry-submit-btn' => 'background-color: {{VALUE}}',
                ],
                'default' => '#E8B04B',
            ]
        );

        $this->end_controls_section();
    }

    protected function render() {
        $settings = $this->get_settings_for_display();

        $form_id = 'travel-inquiry-' . $this->get_id();
        $multi_step = $settings['enable_multi_step'] === 'yes';
        ?>

        <div class="travel-inquiry-form-container">
            <div class="travel-inquiry-form <?php echo esc_attr($settings['form_style']); ?>">

                <?php if (!empty($settings['form_title'])): ?>
                    <h2 class="form-title"><?php echo esc_html($settings['form_title']); ?></h2>
                <?php endif; ?>

                <?php if (!empty($settings['form_description'])): ?>
                    <p class="form-description"><?php echo esc_html($settings['form_description']); ?></p>
                <?php endif; ?>

                <form id="<?php echo esc_attr($form_id); ?>" class="inquiry-form" method="post">
                    <?php wp_nonce_field('travel_inquiry_nonce', 'travel_inquiry_nonce'); ?>

                    <?php if ($multi_step): ?>
                        <!-- 多步驟表單 -->
                        <div class="form-progress">
                            <div class="progress-bar">
                                <div class="progress-fill"></div>
                            </div>
                            <div class="step-indicators">
                                <span class="step-indicator active" data-step="1">1</span>
                                <span class="step-indicator" data-step="2">2</span>
                                <span class="step-indicator" data-step="3">3</span>
                            </div>
                        </div>

                        <!-- 步驟 1: 旅遊類型 -->
                        <div class="form-step active" data-step="1">
                            <h3>選擇旅遊類型</h3>
                            <div class="travel-type-grid">
                                <label class="travel-type-card">
                                    <input type="radio" name="travel_type" value="romantic" required>
                                    <div class="card-content">
                                        <i class="fas fa-heart"></i>
                                        <h4>浪漫蜜月</h4>
                                        <p>情侶旅行</p>
                                    </div>
                                </label>

                                <label class="travel-type-card">
                                    <input type="radio" name="travel_type" value="family" required>
                                    <div class="card-content">
                                        <i class="fas fa-users"></i>
                                        <h4>親子家庭</h4>
                                        <p>家庭旅遊</p>
                                    </div>
                                </label>

                                <label class="travel-type-card">
                                    <input type="radio" name="travel_type" value="senior" required>
                                    <div class="card-content">
                                        <i class="fas fa-leaf"></i>
                                        <h4>樂齡深度</h4>
                                        <p>文化體驗</p>
                                    </div>
                                </label>

                                <label class="travel-type-card">
                                    <input type="radio" name="travel_type" value="business" required>
                                    <div class="card-content">
                                        <i class="fas fa-briefcase"></i>
                                        <h4>商務會議</h4>
                                        <p>MICE服務</p>
                                    </div>
                                </label>
                            </div>
                            <button type="button" class="btn-next">下一步</button>
                        </div>

                        <!-- 步驟 2: 基本需求 -->
                        <div class="form-step" data-step="2">
                            <h3>基本旅遊需求</h3>
                            <div class="form-row">
                                <div class="form-group">
                                    <label for="departure_date">出發時間</label>
                                    <input type="date" id="departure_date" name="departure_date" required>
                                </div>
                                <div class="form-group">
                                    <label for="duration">旅遊天數</label>
                                    <select id="duration" name="duration" required>
                                        <option value="">請選擇</option>
                                        <option value="3-5">3-5天</option>
                                        <option value="6-10">6-10天</option>
                                        <option value="11-15">11-15天</option>
                                        <option value="16+">16天以上</option>
                                    </select>
                                </div>
                            </div>

                            <div class="form-row">
                                <div class="form-group">
                                    <label for="group_size">參與人數</label>
                                    <input type="number" id="group_size" name="group_size" min="1" max="50" required>
                                </div>
                                <div class="form-group">
                                    <label for="budget_range">預算範圍</label>
                                    <select id="budget_range" name="budget_range" required>
                                        <option value="">請選擇</option>
                                        <option value="50000-">5萬以下</option>
                                        <option value="50000-100000">5-10萬</option>
                                        <option value="100000-200000">10-20萬</option>
                                        <option value="200000+">20萬以上</option>
                                    </select>
                                </div>
                            </div>

                            <div class="form-navigation">
                                <button type="button" class="btn-prev">上一步</button>
                                <button type="button" class="btn-next">下一步</button>
                            </div>
                        </div>

                        <!-- 步驟 3: 聯絡資訊 -->
                        <div class="form-step" data-step="3">
                            <h3>聯絡資訊</h3>

                            <div class="form-group">
                                <label for="customer_name">姓名 *</label>
                                <input type="text" id="customer_name" name="customer_name" required>
                            </div>

                            <div class="form-row">
                                <div class="form-group">
                                    <label for="phone">電話 *</label>
                                    <input type="tel" id="phone" name="phone" required>
                                </div>
                                <div class="form-group">
                                    <label for="email">Email *</label>
                                    <input type="email" id="email" name="email" required>
                                </div>
                            </div>

                            <div class="form-group">
                                <label for="preferred_destinations">偏好目的地</label>
                                <input type="text" id="preferred_destinations" name="preferred_destinations" placeholder="例：日本、歐洲、東南亞...">
                            </div>

                            <div class="form-group">
                                <label for="special_requirements">特殊需求</label>
                                <textarea id="special_requirements" name="special_requirements" rows="4" placeholder="如：素食、輪椅、慶祝紀念日等特殊需求"></textarea>
                            </div>

                            <div class="form-group">
                                <label for="contact_preference">偏好聯絡方式</label>
                                <select id="contact_preference" name="contact_preference">
                                    <option value="phone">電話</option>
                                    <option value="email">Email</option>
                                    <option value="line">LINE</option>
                                    <option value="whatsapp">WhatsApp</option>
                                </select>
                            </div>

                            <div class="form-navigation">
                                <button type="button" class="btn-prev">上一步</button>
                                <button type="submit" class="inquiry-submit-btn">提交諮詢</button>
                            </div>
                        </div>

                    <?php else: ?>
                        <!-- 單步驟表單 -->
                        <div class="form-row">
                            <div class="form-group">
                                <label for="customer_name">姓名 *</label>
                                <input type="text" id="customer_name" name="customer_name" required>
                            </div>
                            <div class="form-group">
                                <label for="phone">電話 *</label>
                                <input type="tel" id="phone" name="phone" required>
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="email">Email *</label>
                            <input type="email" id="email" name="email" required>
                        </div>

                        <div class="form-group">
                            <label for="inquiry_message">諮詢內容</label>
                            <textarea id="inquiry_message" name="inquiry_message" rows="5" placeholder="請描述您的旅遊需求..." required></textarea>
                        </div>

                        <button type="submit" class="inquiry-submit-btn">立即諮詢</button>
                    <?php endif; ?>
                </form>

                <!-- 載入動畫 -->
                <div class="form-loading" style="display: none;">
                    <div class="loading-spinner"></div>
                    <p>正在提交您的諮詢...</p>
                </div>

                <!-- 成功訊息 -->
                <div class="form-success" style="display: none;">
                    <div class="success-icon">
                        <i class="fas fa-check-circle"></i>
                    </div>
                    <h3>諮詢已成功提交！</h3>
                    <p>我們的專業顧問將在24小時內與您聯繫</p>
                    <p class="contact-info">
                        急件請直撥：<a href="tel:+886-2-xxxx-xxxx">02-xxxx-xxxx</a><br>
                        或加LINE：<a href="https://line.me/ti/p/@naturetour" target="_blank">@naturetour</a>
                    </p>
                </div>
            </div>
        </div>

        <style>
        .travel-inquiry-form-container {
            max-width: 600px;
            margin: 0 auto;
            padding: 2rem;
        }

        .travel-inquiry-form {
            background: #FFFFFF;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(44, 95, 65, 0.15);
            padding: 2rem;
        }

        .form-title {
            text-align: center;
            color: #2C5F41;
            margin-bottom: 1rem;
        }

        .form-description {
            text-align: center;
            color: #5D6D7E;
            margin-bottom: 2rem;
        }

        .form-progress {
            margin-bottom: 2rem;
        }

        .progress-bar {
            background: #E8E8E8;
            height: 4px;
            border-radius: 2px;
            margin-bottom: 1rem;
            position: relative;
        }

        .progress-fill {
            background: linear-gradient(to right, #2C5F41, #4A8066);
            height: 100%;
            border-radius: 2px;
            transition: width 0.3s ease;
            width: 33.33%;
        }

        .step-indicators {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .step-indicator {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: #E8E8E8;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .step-indicator.active {
            background: #2C5F41;
            color: white;
        }

        .form-step {
            display: none;
        }

        .form-step.active {
            display: block;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .travel-type-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }

        .travel-type-card {
            background: #F4F7F5;
            border: 2px solid #E8E8E8;
            border-radius: 12px;
            padding: 1.5rem 1rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .travel-type-card:hover {
            border-color: #2C5F41;
            transform: translateY(-2px);
        }

        .travel-type-card input[type="radio"] {
            display: none;
        }

        .travel-type-card input[type="radio"]:checked + .card-content {
            color: #2C5F41;
        }

        .travel-type-card input[type="radio"]:checked + .card-content i {
            color: #E8B04B;
        }

        .travel-type-card i {
            font-size: 2rem;
            margin-bottom: 0.5rem;
            color: #5D6D7E;
            transition: color 0.3s ease;
        }

        .travel-type-card h4 {
            margin-bottom: 0.25rem;
            font-size: 1rem;
        }

        .travel-type-card p {
            font-size: 0.875rem;
            color: #85929E;
            margin: 0;
        }

        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .form-group {
            margin-bottom: 1rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: #2C3E50;
        }

        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 0.75rem;
            border: 2px solid #E8E8E8;
            border-radius: 8px;
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }

        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #2C5F41;
        }

        .form-navigation {
            display: flex;
            justify-content: space-between;
            margin-top: 2rem;
        }

        .btn-prev,
        .btn-next,
        .inquiry-submit-btn {
            padding: 0.75rem 2rem;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn-prev {
            background: transparent;
            color: #2C5F41;
            border: 2px solid #2C5F41;
        }

        .btn-next,
        .inquiry-submit-btn {
            background: linear-gradient(135deg, #E8B04B, #D4A043);
            color: white;
        }

        .btn-prev:hover,
        .btn-next:hover,
        .inquiry-submit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        .form-loading {
            text-align: center;
            padding: 2rem;
        }

        .loading-spinner {
            width: 40px;
            height: 40px;
            border: 4px solid #E8E8E8;
            border-top: 4px solid #2C5F41;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .form-success {
            text-align: center;
            padding: 2rem;
        }

        .success-icon i {
            font-size: 4rem;
            color: #27AE60;
            margin-bottom: 1rem;
        }

        .form-success h3 {
            color: #2C5F41;
            margin-bottom: 1rem;
        }

        .contact-info {
            margin-top: 1.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid #E8E8E8;
            color: #5D6D7E;
        }

        .contact-info a {
            color: #2C5F41;
            text-decoration: none;
            font-weight: 600;
        }

        @media (max-width: 768px) {
            .travel-inquiry-form-container {
                padding: 1rem;
            }

            .form-row {
                grid-template-columns: 1fr;
            }

            .travel-type-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .form-navigation {
                flex-direction: column;
                gap: 1rem;
            }
        }
        </style>

        <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('<?php echo esc_js($form_id); ?>');
            if (!form) return;

            <?php if ($multi_step): ?>
            // 多步驟表單邏輯
            let currentStep = 1;
            const totalSteps = 3;

            const nextButtons = form.querySelectorAll('.btn-next');
            const prevButtons = form.querySelectorAll('.btn-prev');

            nextButtons.forEach(btn => {
                btn.addEventListener('click', function() {
                    if (validateCurrentStep()) {
                        goToStep(currentStep + 1);
                    }
                });
            });

            prevButtons.forEach(btn => {
                btn.addEventListener('click', function() {
                    goToStep(currentStep - 1);
                });
            });

            function goToStep(step) {
                if (step < 1 || step > totalSteps) return;

                // 隱藏當前步驟
                form.querySelector(`.form-step[data-step="${currentStep}"]`).classList.remove('active');

                // 顯示新步驟
                form.querySelector(`.form-step[data-step="${step}"]`).classList.add('active');

                // 更新進度指示器
                updateProgressIndicators(step);

                currentStep = step;
            }

            function updateProgressIndicators(step) {
                const indicators = form.querySelectorAll('.step-indicator');
                const progressFill = form.querySelector('.progress-fill');

                indicators.forEach((indicator, index) => {
                    if (index + 1 <= step) {
                        indicator.classList.add('active');
                    } else {
                        indicator.classList.remove('active');
                    }
                });

                const progressPercent = (step / totalSteps) * 100;
                progressFill.style.width = progressPercent + '%';
            }

            function validateCurrentStep() {
                const currentStepElement = form.querySelector(`.form-step[data-step="${currentStep}"]`);
                const requiredFields = currentStepElement.querySelectorAll('[required]');

                for (let field of requiredFields) {
                    if (!field.value) {
                        field.focus();
                        return false;
                    }
                }
                return true;
            }
            <?php endif; ?>

            // 表單提交
            form.addEventListener('submit', function(e) {
                e.preventDefault();

                const formData = new FormData(form);
                formData.append('action', 'handle_travel_inquiry');

                // 顯示載入動畫
                form.style.display = 'none';
                form.parentNode.querySelector('.form-loading').style.display = 'block';

                // Ajax 提交
                fetch('<?php echo admin_url('admin-ajax.php'); ?>', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    // 隱藏載入動畫
                    form.parentNode.querySelector('.form-loading').style.display = 'none';

                    if (data.success) {
                        // 顯示成功訊息
                        form.parentNode.querySelector('.form-success').style.display = 'block';
                    } else {
                        // 顯示錯誤並恢復表單
                        alert('提交失敗，請稍後再試或直接聯繫我們');
                        form.style.display = 'block';
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    form.parentNode.querySelector('.form-loading').style.display = 'none';
                    form.style.display = 'block';
                    alert('提交失敗，請檢查網路連線');
                });
            });
        });
        </script>
        <?php
    }
}

// Ajax 處理函數
add_action('wp_ajax_handle_travel_inquiry', 'handle_travel_inquiry_submission');
add_action('wp_ajax_nopriv_handle_travel_inquiry', 'handle_travel_inquiry_submission');

function handle_travel_inquiry_submission() {
    // 驗證 nonce
    if (!wp_verify_nonce($_POST['travel_inquiry_nonce'], 'travel_inquiry_nonce')) {
        wp_die('安全驗證失敗');
    }

    // 清理並驗證表單數據
    $customer_name = sanitize_text_field($_POST['customer_name']);
    $phone = sanitize_text_field($_POST['phone']);
    $email = sanitize_email($_POST['email']);

    if (empty($customer_name) || empty($phone) || empty($email)) {
        wp_send_json_error('請填寫必要欄位');
    }

    // 儲存到資料庫
    global $wpdb;

    $table_name = $wpdb->prefix . 'travel_inquiries';

    $inquiry_data = array(
        'customer_name' => $customer_name,
        'phone' => $phone,
        'email' => $email,
        'travel_type' => sanitize_text_field($_POST['travel_type'] ?? ''),
        'departure_date' => sanitize_text_field($_POST['departure_date'] ?? ''),
        'duration' => sanitize_text_field($_POST['duration'] ?? ''),
        'group_size' => absint($_POST['group_size'] ?? 0),
        'budget_range' => sanitize_text_field($_POST['budget_range'] ?? ''),
        'preferred_destinations' => sanitize_text_field($_POST['preferred_destinations'] ?? ''),
        'special_requirements' => sanitize_textarea_field($_POST['special_requirements'] ?? ''),
        'contact_preference' => sanitize_text_field($_POST['contact_preference'] ?? 'phone'),
        'inquiry_message' => sanitize_textarea_field($_POST['inquiry_message'] ?? ''),
        'created_at' => current_time('mysql')
    );

    $result = $wpdb->insert($table_name, $inquiry_data);

    if ($result) {
        // 發送Email通知
        $to = get_option('admin_email');
        $subject = '新的旅遊諮詢 - ' . $customer_name;
        $message = "新的旅遊諮詢：\n\n";
        $message .= "客戶姓名：{$customer_name}\n";
        $message .= "聯絡電話：{$phone}\n";
        $message .= "Email：{$email}\n";

        if (!empty($_POST['travel_type'])) {
            $message .= "旅遊類型：{$_POST['travel_type']}\n";
        }

        wp_mail($to, $subject, $message);

        wp_send_json_success('諮詢提交成功');
    } else {
        wp_send_json_error('提交失敗，請稍後再試');
    }
}

// 建立資料表
register_activation_hook(__FILE__, 'create_travel_inquiries_table');

function create_travel_inquiries_table() {
    global $wpdb;

    $table_name = $wpdb->prefix . 'travel_inquiries';

    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        customer_name tinytext NOT NULL,
        phone varchar(20) NOT NULL,
        email varchar(100) NOT NULL,
        travel_type varchar(50),
        departure_date date,
        duration varchar(20),
        group_size int,
        budget_range varchar(50),
        preferred_destinations text,
        special_requirements text,
        contact_preference varchar(20),
        inquiry_message text,
        status varchar(20) DEFAULT 'pending',
        created_at datetime DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}