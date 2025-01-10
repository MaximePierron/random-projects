<?php
/**
 * SpecialHoverCard class.
 *
 * @category   Class
 * @package    ElementorCustom
 * @subpackage WordPress
 * @author     Maxime Pierron <maxime@pierron.com>
 * @copyright  2023 Maxime Pierron
 * @license    https://opensource.org/licenses/GPL-3.0 GPL-3.0-only
 * @link       link(https://example.com/,
 *             Build Custom Elementor Widgets)
 * @since      1.0.0
 * php version 8.2.3
 */
namespace ElementorCustom\Widgets;

use ElementorPro\Base\Base_Widget;
use Elementor\Controls_Manager;
// Security Note: Blocks direct access to the plugin PHP files.
defined( 'ABSPATH' ) || die();
/**
 * SpecialHoverCard widget class.
 *
 * @since 1.0.0
 */
class SpecialHoverCard extends Base_Widget {
	/**
	 * Class constructor.
	 *
	 * @param array $data Widget data.
	 * @param array $args Widget arguments.
	 */
	public function __construct( $data = array(), $args = null ) {
		parent::__construct( $data, $args );
		wp_register_style( 'specialhovercard', plugins_url( '/assets/css/specialhovercard.css', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
		wp_register_script( 'specialhovercard', plugins_url( '/assets/js/specialhovercard.js', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
	}
	/**
	 * Retrieve the widget name.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget name.
	 */
	public function get_name() {
		return 'special-hover-card';
	}
	/**
	 * Retrieve the widget title.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget title.
	 */
	public function get_title() {
		return __( 'Special Hover Card', 'elementor-custom' );
	}
	/**
	 * Retrieve the widget icon.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget icon.
	 */
	public function get_icon() {
		return 'eicon-blockquote';
	}
	/**
	 * Retrieve the list of categories the widget belongs to.
	 *
	 * Used to determine where to display the widget in the editor.
	 *
	 * Note that currently Elementor supports only one category.
	 * When multiple categories passed, Elementor uses the first one.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return array Widget categories.
	 */
	public function get_categories() {
		return array( 'elementor-custom-widgets' );
	}
	
	/**
	 * Enqueue styles.
	 */
	public function get_style_depends() {
		return array( 'specialhovercard' );
	}
	/**
	 * Enqueue scripts.
	 */
	public function get_script_depends() {
		if (\Elementor\Plugin::$instance->editor->is_edit_mode() || \Elementor\Plugin::$instance->preview->is_preview_mode()) {
			return [];
		} else {
			return array( 'specialhovercard' );
		}
		
	}

	/**
	 * Register the widget controls.
	 *
	 * Adds different input fields to allow the user to change and customize the widget settings.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function _register_controls() {

		$this->start_controls_section(
			'content_section',
			[
				'label' => __( 'Content', 'elementor-custom' ),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);

		$this->add_control(
			'card_title',
			[
				'label' => esc_html__( 'Add a title', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::TEXT,
				'default' => esc_html__( 'I know exactly what I\'m doing' , 'elementor-custom' ),
				'label_block' => true,
			]
		);

        $this->add_control(
			'card_sub_title',
			[
				'label' => esc_html__( 'Add a sub title', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::TEXT,
				'default' => esc_html__( 'But in a much more real sense, I have no idea what I\'m doing.' , 'elementor-custom' ),
				'label_block' => true,
			]
		);

        
        $this->add_control(
			'icon',
			[
				'label' => esc_html__( 'Icon', 'textdomain' ),
				'type' => \Elementor\Controls_Manager::ICONS,
			]
		);

		$this->end_controls_section();
	}
	/**
	 * Render the widget output on the frontend.
	 *
	 * Written in PHP and used to generate the final HTML.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function render() {
		$settings = $this->get_settings_for_display();
        echo '<script> const subtitleText = "' . $settings['card_sub_title'] . '";</script>';
        ?>
        <div class="card">
            <div class="card-content">
                <?php
                echo '<h3 class="card-title">' . $settings['card_title'] . '</h3>';
                ?>
                <h4 class="card-subtitle"></h4>
            </div>
            <div class="card-icon">
                <?php \Elementor\Icons_Manager::render_icon( $settings['icon'], [ 'aria-hidden' => 'true' ] ); ?>
            </div>
        </div>
        <?php
	}

	protected function content_template() {
		?>
        <#
		    var iconHTML = elementor.helpers.renderIcon( view, settings.selected_icon, { 'aria-hidden': true }, 'i' , 'object' );
		#>
        <script> const subtitleText = "{{ settings.card_sub_title }}";</script>
        <div class="card">
            <div class="card-content">
                <h3 class="card-title">{{{ settings.card_title }}}</h3>
                <h4 class="card-subtitle"></h4>
            </div>
            <div class="card-icon">
                {{{ iconHTML.value }}}
            </div>
        </div>
		<?php
	}
}