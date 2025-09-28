<?php
/**
 * Elementor 自訂小工具載入器
 *
 * @package NatureTour
 * @version 1.0.0
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * 主要 Elementor 小工具類別
 */
final class NatureTour_Elementor_Widgets {

    const VERSION = '1.0.0';
    const MINIMUM_ELEMENTOR_VERSION = '3.0.0';
    const MINIMUM_PHP_VERSION = '7.4';

    private static $_instance = null;

    public static function instance() {
        if (is_null(self::$_instance)) {
            self::$_instance = new self();
        }
        return self::$_instance;
    }

    public function __construct() {
        add_action('plugins_loaded', [$this, 'init']);
    }

    public function init() {
        // 檢查 Elementor 是否已安裝並啟用
        if (!did_action('elementor/loaded')) {
            add_action('admin_notices', [$this, 'admin_notice_missing_main_plugin']);
            return;
        }

        // 檢查 Elementor 版本
        if (!version_compare(ELEMENTOR_VERSION, self::MINIMUM_ELEMENTOR_VERSION, '>=')) {
            add_action('admin_notices', [$this, 'admin_notice_minimum_elementor_version']);
            return;
        }

        // 檢查 PHP 版本
        if (version_compare(PHP_VERSION, self::MINIMUM_PHP_VERSION, '<')) {
            add_action('admin_notices', [$this, 'admin_notice_minimum_php_version']);
            return;
        }

        // 新增 Elementor 小工具類別
        add_action('elementor/widgets/widgets_registered', [$this, 'register_widgets']);

        // 新增 Elementor 控制項
        add_action('elementor/controls/controls_registered', [$this, 'register_controls']);

        // 註冊小工具類別
        add_action('elementor/elements/categories_registered', [$this, 'add_elementor_widget_categories']);
    }

    /**
     * 管理員通知：缺少 Elementor
     */
    public function admin_notice_missing_main_plugin() {
        if (isset($_GET['activate'])) unset($_GET['activate']);

        $message = sprintf(
            esc_html__('"%1$s" 需要 "%2$s" 才能運作。', 'naturetour'),
            '<strong>' . esc_html__('NatureTour Elementor Widgets', 'naturetour') . '</strong>',
            '<strong>' . esc_html__('Elementor', 'naturetour') . '</strong>'
        );

        printf('<div class="notice notice-warning is-dismissible"><p>%1$s</p></div>', $message);
    }

    /**
     * 管理員通知：Elementor 版本過低
     */
    public function admin_notice_minimum_elementor_version() {
        if (isset($_GET['activate'])) unset($_GET['activate']);

        $message = sprintf(
            esc_html__('"%1$s" 需要 "%2$s" 版本 %3$s 或更高版本。', 'naturetour'),
            '<strong>' . esc_html__('NatureTour Elementor Widgets', 'naturetour') . '</strong>',
            '<strong>' . esc_html__('Elementor', 'naturetour') . '</strong>',
            self::MINIMUM_ELEMENTOR_VERSION
        );

        printf('<div class="notice notice-warning is-dismissible"><p>%1$s</p></div>', $message);
    }

    /**
     * 管理員通知：PHP 版本過低
     */
    public function admin_notice_minimum_php_version() {
        if (isset($_GET['activate'])) unset($_GET['activate']);

        $message = sprintf(
            esc_html__('"%1$s" 需要 "%2$s" 版本 %3$s 或更高版本。', 'naturetour'),
            '<strong>' . esc_html__('NatureTour Elementor Widgets', 'naturetour') . '</strong>',
            '<strong>' . esc_html__('PHP', 'naturetour') . '</strong>',
            self::MINIMUM_PHP_VERSION
        );

        printf('<div class="notice notice-warning is-dismissible"><p>%1$s</p></div>', $message);
    }

    /**
     * 註冊小工具
     */
    public function register_widgets() {
        // 包含小工具檔案
        require_once(__DIR__ . '/travel-inquiry-form/travel-inquiry-form.php');
        require_once(__DIR__ . '/destination-showcase/destination-showcase.php');
        require_once(__DIR__ . '/testimonial-carousel/testimonial-carousel.php');
        require_once(__DIR__ . '/tour-package-grid/tour-package-grid.php');
        require_once(__DIR__ . '/travel-blog-posts/travel-blog-posts.php');

        // 註冊小工具
        \Elementor\Plugin::instance()->widgets_manager->register_widget_type(new \Travel_Inquiry_Form_Widget());
        \Elementor\Plugin::instance()->widgets_manager->register_widget_type(new \Destination_Showcase_Widget());
        \Elementor\Plugin::instance()->widgets_manager->register_widget_type(new \Testimonial_Carousel_Widget());
        \Elementor\Plugin::instance()->widgets_manager->register_widget_type(new \Tour_Package_Grid_Widget());
        \Elementor\Plugin::instance()->widgets_manager->register_widget_type(new \Travel_Blog_Posts_Widget());
    }

    /**
     * 註冊控制項
     */
    public function register_controls() {
        // 如需自訂控制項，在此註冊
    }

    /**
     * 新增小工具類別
     */
    public function add_elementor_widget_categories($elements_manager) {
        $elements_manager->add_category(
            'naturetour',
            [
                'title' => esc_html__('NatureTour 旅遊', 'naturetour'),
                'icon' => 'fa fa-plug',
            ]
        );
    }
}

// 初始化
NatureTour_Elementor_Widgets::instance();