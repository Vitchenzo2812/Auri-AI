import { motion } from 'framer-motion'
import { BaseAnimationIconProps } from './base'

const AuriIcon = (props: BaseAnimationIconProps) => {
  return (
    <motion.svg
      xmlns="http://www.w3.org/2000/svg"
      width="14"
      height="15"
      fill="none"
      viewBox="0 0 14 15"
      {...props}
    >
      <motion.path
        fill="#121417"
        fillRule="evenodd"
        d="M7 .833A8.2 8.2 0 0 0 13.667 7.5 8.2 8.2 0 0 0 7 14.167 8.2 8.2 0 0 0 .333 7.5 8.2 8.2 0 0 0 7 .833"
        clipRule="evenodd"
      />
    </motion.svg>
  )
}

export default AuriIcon
